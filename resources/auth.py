from flask import Response, request
from flask_jwt_extended import create_access_token
from database.models import User
from flask_restful import Resource
import datetime

from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist
from resources.errors import SchemaValidationError, EmailAlreadyExistsError, \
    UnauthorizedError, InternalServerError

class SignupApi(Resource):
    def post(self):
        try:
            body = request.get_json(force=True)
            user = User(**body)
            user.hash_password()
            user.save()
            id = user.id
            return {"id" : str(id)}, 200
        except FieldDoesNotExist:
            raise SchemaValidationError
        except NotUniqueError:
            raise EmailAlreadyExistsError
        except Exception as e:
            print(e.message, e.args)


class LoginApi(Resource):
    def post(self):
        try:
            body = request.get_json(force=True)
            user = User.objects.get(email=body.get("email"))
            authorized = user.check_password(body.get("password"))

            if not authorized:
                return {"error" : "Email or password is invalid"}, 401
            
            expires = datetime.timedelta(days=7)
            access_token = create_access_token(identity=str(user.id), expires_delta=expires)

            return {"token" : access_token}, 200
        except (UnauthorizedError, DoesNotExist):
            raise UnauthorizedError
        except Exception as e:
            print(e.message, e.args)