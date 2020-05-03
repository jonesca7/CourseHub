from flask import Flask, render_template
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from database.db import initialize_db
from flask_restful import Api
from resources.routes import initialize_routes
from resources.errors import errors
from pymongo import MongoClient

app = Flask(__name__)
app.config.from_envvar('ENV_FILE_LOCATION')
api = Api(app, errors=errors)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

db_client = MongoClient('mongodb+srv://jonesca7:tohacks2020@coursehub-8qtyk.gcp.mongodb.net/test?retryWrites=true&w=majority')
db = db_client.CourseList #Create database 
harvard = db.harvard #Create collection called harvard

# TODO update to cluster in atlas
# mongodb+srv://jonesca7:tohacks2020@coursehub-8qtyk.gcp.mongodb.net/test?retryWrites=true&w=majority

# below is on Racheal's local machine
app.config['MONGODB_SETTINGS'] = {
    "db": "course-hub",
    'host': 'mongodb://localhost:27017/course-hub'
}

initialize_db(app)
initialize_routes(api)

@app.route("/")
def index():
    courses = harvard.find()
    return render_template("index.html", courses=courses)

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
# export ENV_FILE_LOCATION=./.env
# python3 app.py