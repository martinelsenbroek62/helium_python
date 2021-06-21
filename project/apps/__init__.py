from flask_migrate import Migrate
from helium_flask.project.project.initialize_app import app, db
from helium_flask.project.apps.claims.models import Claims
migrate = Migrate(app, db)


# #!/usr/bin/env python3
#
# import bcrypt
#
# passwd = b'secret'
#
# salt = bcrypt.gensalt()
# hashed = bcrypt.hashpw(passwd, salt)
#
# print(salt)
# print(hashed)