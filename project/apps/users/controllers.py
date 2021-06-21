from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, login_required, current_user, logout_user
from flask_mail import Message
from werkzeug.security import check_password_hash, generate_password_hash

from .forms import LoginForm, ProfileForm, ForgotPasswordForm, ResetPasswordForm
from .models import User
from helium_flask.project.apps import db
from helium_flask.project.helpers.users import mail
from helium_flask.project.helpers.users import ts

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
        current_user.query.update({'email': request.form.get("email"), 'username': request.form.get("username"), 'name': request.form.get("name")})
        db.session.commit()
        return render_template('profile.html', user=current_user, form=form)
    else:
        return render_template('profile.html', user=current_user, form=form)



# @user_router.route('send_mail/', methods=["POST"])
# def send_mail():
#     email = request.form.get("email")
#     if User.query.filter(email==email).count():
#         msg = Message('Hello', sender='oldnightsproject@gmail.com', recipients=[email])
#         msg.body = "Hello Flask message sent from Flask-Mail"
#         mail.send(msg)
#         resp = "Sent!"
#     else:
#         resp = "No user with this email exists!"
#     flash(resp)
#     return redirect(url_for('user_router.forgot_password'))




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
        msg = Message('Password Reset', sender='oldnightsproject@gmail.com', recipients=[email])
        msg.body = render_template(
            'password_reset_mail_template.html',
            password_reset_url=password_reset_url)
        mail.send(msg)
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
@user_router.route('', methods=['GET', 'POST'])
def create_user():
    if request.form:
        user = User(email=request.form.get("email"),
                    password=generate_password_hash(request.form.get("password"),  method='sha256'))
        user.save()
        return redirect(url_for('user_router.login'))
    else:
        return render_template("create.html")


@user_router.route('delete/')
def delete_users():
    for user in User.query.all():
        user.delete()
    return render_template("create.html")

# @user_router.route("/pwresetrq", methods=["POST"])
# def pwresetrq_post():
#     if db.session.query(User).filter_by(email=request.form["email"]).first():
#         user = db.session.query(User).filter_by(email=request.form["email"]).one()
#         # check if user already has reset their password, so they will update
#         # the current key instead of generating a separate entry in the table.
#         if db.session.query(PWReset).filter_by(user_id=user.id).first():
#             pwalready = db.session.query(PWReset).filter_by(user_id=user.id).first()
#             # if the key hasn't been used yet, just send the same key.
#             if pwalready.has_activated == False:
#                 pwalready.datetime = datetime.now()
#                 key = pwalready.reset_key
#             else:
#                 key = keygenerator.make_key()
#                 pwalready.reset_key = key
#                 pwalready.datetime = datetime.now()
#                 pwalready.has_activated = False
#         else:
#             key = keygenerator.make_key()
#             user_reset = PWReset(reset_key=key, user_id=user.id)
#             db.session.add(user_reset)
#         db.session.commit()
#         return redirect(url_for("entries"))
#     else:
#         flash("Your email was never registered.", "danger")
#         return redirect(url_for("pwresetrq_get"))

# @app.route("/pwreset/<id>", methods=["GET"])
# def pwreset_get(id):
#     key = id
#     pwresetkey = session.query(PWReset).filter_by(reset_key=id).one()
#     generated_by = datetime.utcnow().replace(tzinfo=pytz.utc) - timedelta(hours=24)
#     if pwresetkey.has_activated is True:
#         flash("You already reset your password with the URL you are using." +
#               "If you need to reset your password again, please make a" +
#               " new request here.", "danger")
#         return redirect(url_for("pwresetrq_get"))
#     if pwresetkey.datetime.replace(tzinfo=pytz.utc) < generated_by:
#         flash("Your password reset link expired.  Please generate a new one" +
#               " here.", "danger")
#         return redirect(url_for("pwresetrq_get"))
#     return render_template('pwreset.html', id=key)

# @app.route("/pwreset/<id>", methods=["POST"])
# def pwreset_post(id):
#     if request.form["password"] != request.form["password2"]:
#     flash("Your password and password verification didn't match."
#           , "danger")
#     return redirect(url_for("pwreset_get", id=id))
#     if len(request.form["password"]) < 8:
#         flash("Your password needs to be at least 8 characters", "danger")
#         return redirect(url_for("pwreset_get", id=id))
#     user_reset = session.query(PWReset).filter_by(reset_key=id).one()
#     try:
#         exists(session.query(User).filter_by(id = user_reset.user_id)
#                .update({'password':
#                         generate_password_hash(request.form["password"])}))
#         session.commit(exists)
#     except IntegrityError:
#         flash("Something went wrong", "danger")
#         session.rollback()
#         return redirect(url_for("entries"))
#     user_reset.has_activated = True
#     session.commit()
#     flash("Your new password is saved.", "success")
#     return redirect(url_for("entries")

# temporary, will be replaced by an admin panel
