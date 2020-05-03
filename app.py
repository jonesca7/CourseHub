from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from database.db import initialize_db
from flask_restful import Api
from resources.routes import initialize_routes
from resources.errors import errors

app = Flask(__name__)
app.config.from_envvar('ENV_FILE_LOCATION')
api = Api(app, errors=errors)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

# TODO update to cluster in atlas
# mongodb+srv://jonesca7:tohacks2020@coursehub-8qtyk.gcp.mongodb.net/test?retryWrites=true&w=majority

# below is on Racheal's local machine
app.config['MONGODB_SETTINGS'] = {
    "db": "course-hub",
    'host': 'mongodb://localhost:27017/course-hub'
}

initialize_db(app)
initialize_routes(api)

app.run()

# INSTRUCTIONS
# Download Postman from https://www.postman.com/ to test API
# Tutorial series: https://dev.to/paurakhsharma/flask-rest-api-part-0-setup-basic-crud-api-4650

# Installing Flask and Mongo requirements on your machine
# sudo -H pip install -U pipenv
# pipenv install flask
# pipenv install flask-mongoengine
# pipenv install flask-restful
# pipenv install flask-bcrypt
# pipenv install flask-jwt-extended
# pip install python-dotenv

# Type below in terminal to run the app
# mongod (to start db server)
# Type following in a new terminal window
# pipenv shell
# python3 app.py