from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, login_required, current_user, logout_user
from flask_mail import Message
from werkzeug.security import check_password_hash, generate_password_hash

from .forms import LoginForm, ProfileForm, ForgotPasswordForm, ResetPasswordForm, UserSignupForm
from .models import User
from helium_flask.project.apps import db
from helium_flask.project.helpers.users_helpers import mail
from helium_flask.project.helpers.users_helpers import ts
from helium_flask.project.project.initialize_app import app

user_router = Blueprint('user_router', __name__,
                        template_folder='../../templates/users')


@user_router.route('login/', methods=['GET', 'POST'])
def login():
    if request.form:
        email = request.form.get('email')
        password = request.form.get('password')
        remember = True if request.form.get('remember') else False

        user = User.query.filter_by(email=email).first()
        if not user or not check_password_hash(user.password, password):
            flash('Please check your login details and try again.')
            return redirect(url_for('user_router.login'))

        login_user(user, remember=remember)
        return redirect(url_for('general_router.home'))
    else:
        if current_user.is_authenticated:
            return redirect(url_for("general_router.home"))
        return render_template("login.html", form=LoginForm())


@user_router.route('logout/')
@login_required
def logout():
    logout_user()
    return redirect(url_for('user_router.login'))

@user_router.route('profile/', methods=['GET', 'POST'])
@login_required
def profile():
    form = ProfileForm()
    if request.form:
        update_dict = {'email': request.form.get("email"), "name": request.form.get("name"),
                                   }
        if request.form.get("password"):
            update_dict["password"] = generate_password_hash(request.form.get("password"), method='sha256')
        current_user.query.update(update_dict)
        db.session.commit()
        return render_template('profile.html', user=current_user, form=form)
    else:
        return render_template('profile.html', user=current_user, form=form, placeholders={
            "email": current_user.email,
            "name": current_user.name,
            "password": current_user.password
        })

@user_router.route('forgot_password/')
def forgot_password():
    return render_template("forgot_password.html", form=ForgotPasswordForm())

@user_router.route('send_password_reset_mail/', methods=["POST"])
def send_password_reset_email():
    email = request.form.get("email")
    if User.query.filter(email==email).count():
        password_reset_url = url_for(
            'user_router.reset_with_token',
            token=ts.dumps(email, salt='password-reset-key'),
            _external=True)
        msg = Message('Password Reset', sender=app.config['MAIL_USERNAME'], recipients=[email])
        msg.html = render_template(
            'password_reset_mail_template.html',
            password_reset_url=password_reset_url)
        try:
            mail.send(msg)
        except:
            resp = "Mail couldn't be sent!"
        else:
            resp = "Sent!"
    else:
        resp = "No user with this email exists!"
    flash(resp)
    return redirect(url_for('user_router.forgot_password'))


@user_router.route('reset/<token>', methods=["GET", "POST"])
def reset_with_token(token):
    email = ts.loads(token, salt="password-reset-key", max_age=86400)

    form = ResetPasswordForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=email).first_or_404()

        # compare passwords and display flash messages
        user.password = form.password.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('user_router.login'))

    return render_template('reset_password.html', form=form, token=token)

# @user_router.route("reset_password/", methods=['GET', 'POST'])
# def reset_password():
@user_router.route('signup/', methods=['GET', 'POST'])
def signup():
    if request.form:
        if request.form.get("password") == request.form.get("password2"):
            user = User(email=request.form.get("email"),
                        password=generate_password_hash(request.form.get("password"),  method='sha256'))
            user.save()
            return redirect(url_for('user_router.login'))
    else:
        form = UserSignupForm()
        return render_template("signup.html", form=form)


@user_router.route('delete/')
def delete_users():
    for user in User.query.all():
        user.delete()
    return render_template("signup.html")
