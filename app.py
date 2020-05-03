from flask import Flask, render_template, request
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_paginate import Pagination, get_page_parameter
from database.db import initialize_db
from flask_restful import Api
from resources.routes import initialize_routes
from resources.errors import errors
from pymongo import MongoClient

app = Flask(__name__)
#app.config.from_envvar('ENV_FILE_LOCATION')
api = Api(app, errors=errors)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

db_client = MongoClient('mongodb+srv://jonesca7:tohacks2020@coursehub-8qtyk.gcp.mongodb.net/test?retryWrites=true&w=majority')
db = db_client.CourseList #Create database 
collection = db.collection #Create collection called harvard

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
    # search = False
    # q = request.args.get('q')
    # if q:
    #     search = True

    # page = request.args.get(get_page_parameter(), type=int, default=1)
    # # courses = collection.find()
    # courses = collection.find().sort("name",pymongo.ASCENDING)   
    # pagination = Pagination(page=page, total=courses.count(), search=search, record_name='courses', css_framework='bootstrap4')
    
    # return render_template("index.html", courses=courses, pagination=pagination)
    
    param = request.args.get('query')
    query = {"name" : param}

    page = request.args.get(get_page_parameter(), type=int, default=1)
    per_page = 20
    offset = (page - 1) * per_page
    print(offset)

    if param is None:
        courses = collection.find().sort("name", 1)
    else:
        courses = collection.find({'name':{'$regex': str(param) }}).sort("name", 1)
    courses_for_render = courses.limit(per_page).skip(offset)

    search = False
    q = request.args.get('q')
    if q:
        search = True

    pagination = Pagination(page=page, per_page=per_page, offset=offset,total=courses.count(), search=search,
                            record_name='courses', css_framework='bootstrap4')
    
    return render_template("index.html", courses=courses_for_render, pagination=pagination)

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
# pip install  flask-paginate


# Type below in terminal to run the app
# mongod (to start db server)
# Type following in a new terminal window
# pipenv shell
# export ENV_FILE_LOCATION=./.env
# python3 app.py