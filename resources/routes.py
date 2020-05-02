from .course import CoursesApi, CourseApi

def initialize_routes(api):
    api.add_resource(CoursesApi, "/api/courses")
    api.add_resource(CourseApi, "/api/courses/<id>")