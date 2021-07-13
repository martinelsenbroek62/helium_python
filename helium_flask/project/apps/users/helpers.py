from flask import url_for, render_template_string
from flask_mail import Message

from helium_flask.project.apps.users.const import login_link_message
from helium_flask.project.project.initialize_app import app, mail
from helium_flask.project.apps.users.models import Token



def mail_login_token(email):
    if token := Token.query.filter_by(email=email).first():
        token.delete()
    token = Token(email=email)
    token.save()
    login_url = url_for(
        "user_router.temporary_login", token=token.token_string, _external=True
    )
    print(login_url)
    msg = Message(
        "Password Reset", sender=app.config["MAIL_USERNAME"], recipients=[email]
    )
    msg.html = render_template_string(login_link_message, link=login_url)
    try:
        mail.send(msg)
    except Exception as e:
        token.delete()
        return False
    else:
        return True
