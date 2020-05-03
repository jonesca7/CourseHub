from selenium.webdriver import Chrome
from selenium.common.exceptions import NoSuchElementException
from pymongo import MongoClient

#Set up MongoDB client
db_client = MongoClient('mongodb+srv://jonesca7:tohacks2020@coursehub-8qtyk.gcp.mongodb.net/test?retryWrites=true&w=majority')
db = db_client.CourseList #Select database 
collection = db.collection 

webdriver = "chromedriver.exe"
driver = Chrome(webdriver)

url = "https://www.classcentral.com/report/coursera-free-certificate-covid-19/"
driver.get(url)

course_list = []
courses = driver.find_elements_by_xpath("//section/div/ul/li")
for course in courses:
	course_title = course.find_element_by_xpath("a").text

	try:
		course_platform = course.find_element_by_xpath("em").text
	except NoSuchElementException:
		course_platform = "Unknown"

	course_url = course.find_element_by_xpath("a").get_attribute("href")
	
	course_object = {"name" : course_title, "topic" : "N/A", "platform" : course_platform, "url" : course_url}
	course_list.append(course_object)

collection.insert_many(course_list)

driver.close()