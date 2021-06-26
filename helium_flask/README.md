
### Navigate to root directory, config and run following commands:
```sh
> git clone https://github.com/pyeliteman/helium_python.git

> cd helium_python

> cd helium_flask

> python3 -m pip install pipenv

> pipenv shell

> pipenv install

> export FLASK_APP=run.py

> export FLASK_ENV=development

> export DATABASE_URL=postgresql://<user>:<password>@<host>:<port>/<database_name>

> export MAIL_USERNAME=<email>

> export MAIL_PASSWORD=<password>

> flask db init

> flask db migrate -m "Initial migration."

> flask db upgrade

> flask run
```
 
For signup, go to: http://localhost:5000/users/signup/
