class InternalServerError(Exception):
    pass

class SchemaValidationError(Exception):
    pass

class CourseAlreadyExistsError(Exception):
    pass

class UpdatingCourseError(Exception):
    pass

class DeletingCourseError(Exception):
    pass

class CourseNotExistsError(Exception):
    pass

class EmailAlreadyExistsError(Exception):
    pass

class UnauthorizedError(Exception):
    pass

errors = {
    "InternalServerError": {
        "message": "Something went wrong",
        "status": 500
    },
     "SchemaValidationError": {
         "message": "Request is missing required fields",
         "status": 400
     },
     "CourseAlreadyExistsError": {
         "message": "Course with given name already exists",
         "status": 400
     },
     "UpdatingCourseError": {
         "message": "Updating course added by other is forbidden",
         "status": 403
     },
     "DeletingCourseError": {
         "message": "Deleting course added by other is forbidden",
         "status": 403
     },
     "CourseNotExistsError": {
         "message": "Course with given id doesn't exists",
         "status": 400
     },
     "EmailAlreadyExistsError": {
         "message": "User with given email address already exists",
         "status": 400
     },
     "UnauthorizedError": {
         "message": "Invalid username or password",
         "status": 401
     }
}