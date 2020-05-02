from flask import Response, request
from database.models import Course
from flask_restful import Resource


# JSON Format for a course
# { "name" : "Test Course A",
#   "topic" : "Web Development",
#   "platform" : "Coursera",
#   "url" : "https://www.coursera.org/learn/mindshift"
# }


class CoursesApi(Resource):
    def get(self):
        courses = Course.objects().to_json()
        return Response(courses, mimetype="application/json", status=200)
    
    def post(self):
        body = request.get_json(force=True)
        course = Course(**body).save()
        id = course.id
        return {"id" : str(id)}, 200


# API to interact with a specific course based on id
class CourseApi(Resource):    
    def put(self, id):
        body = request.get_json(force=True)
        Course.objects.get(id=id).update(**body)
        return "", 200
    
    def delete(self, id):
        course = Course.objects.get(id=id).delete()
        return "None", 200
    
    def get(self, id):
        courses = Course.objects.get(id=id).to_json()
        return Response(courses, mimetype="application/json", status=200)