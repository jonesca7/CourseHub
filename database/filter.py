from pymongo import MongoClient




def findCourses(keyword=""):
    client = MongoClient('mongodb+srv://jonesca7:tohacks2020@coursehub-8qtyk.gcp.mongodb.net/test?retryWrites=true&w=majority')

    db = client.CourseList
    harvard = db.harvard
    cursor = harvard.find({
        "name" : {'$regex' : '.*' + keyword + '.*', '$options' : 'i' }
    })

    couseNames = []


    for document in cursor:
        print(document["name"])
        couseNames.append(document["name"])

    return couseNames


if __name__ == '__main__':
    findCourses()