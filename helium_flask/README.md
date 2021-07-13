
### Navigate to root directory, config and run following commands:

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
