from pymongo import MongoClient




def findCourses():
    client = MongoClient('mongodb+srv://jonesca7:tohacks2020@coursehub-8qtyk.gcp.mongodb.net/test?retryWrites=true&w=majority')

    db = client.CourseList
    harvard = db.harvard
    cursor = harvard.find({})
    for document in cursor:
        print(document)






if __name__ == '__main__':
    findCourses()