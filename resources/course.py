from flask import Response, request
from database.models import Course, User
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource


# JSON Format for a course
# { "name" : "Test Course A",
#   "topic" : "Web Development",
#   "platform" : "Coursera",
#   "url" : "https://www.coursera.org/learn/mindshift"
# }


class CoursesApi(Resource):
    def get(self):
        query = Course.objects()
        courses = Course.objects().to_json()
        return Response(courses, mimetype="application/json", status=200)
    
    @jwt_required
    def post(self):
        user_id = get_jwt_identity()
        body = request.get_json(force=True)
        user = User.objects.get(id=user_id)
        course = Course(**body, added_by=user)
        course.save()
        user.update(push__courses=course)
        user.save()
        id = course.id
        return {"id" : str(id)}, 200


# API to interact with a specific course based on id
class CourseApi(Resource):    
    @jwt_required
    def put(self, id):
        user_id = get_jwt_identity()
        course = Course.objects.get(id=id, added_by=user_id)
        body = request.get_json(force=True)
        Course.objects.get(id=id).update(**body)
        return "", 200
    
    @jwt_required
    def delete(self, id):
        user_id = get_jwt_identity()
        course = Course.objects.get(id=id, added_by=user_id)
        course.delete()
        return "None", 200
    
    def get(self, id):
        courses = Course.objects.get(id=id).to_json()
        return Response(courses, mimetype="application/json", status=200)