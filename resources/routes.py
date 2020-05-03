from .course import CoursesApi, CourseApi
from .auth import SignupApi, LoginApi


def initialize_routes(api):
    api.add_resource(CoursesApi, "/api/courses")
    api.add_resource(CourseApi, "/api/courses/<id>")
    
    api.add_resource(SignupApi, "/api/auth/signup")
    api.add_resource(LoginApi, "/api/auth/login")