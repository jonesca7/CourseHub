from harvard import Scrape_Harvard
from coursera import Scrape_Coursera
from futurelearn import Scrape_Futurelearn
from stanford import Scrape_Stanford
from pymongo import MongoClient

db_client = MongoClient('mongodb+srv://jonesca7:tohacks2020@coursehub-8qtyk.gcp.mongodb.net/test?retryWrites=true&w=majority')
db = db_client.CourseList #Get database
collection = db.collection #Get collection

collection.drop() #Drop collection of courses before re-populating

Scrape_Harvard()
Scrape_Stanford()
Scrape_Coursera()
Scrape_Futurelearn()