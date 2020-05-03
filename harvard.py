from selenium.webdriver import Chrome
from pymongo import MongoClient

#Set up MongoDB client
db_client = MongoClient('mongodb+srv://jonesca7:tohacks2020@coursehub-8qtyk.gcp.mongodb.net/test?retryWrites=true&w=majority')
db = db_client.CourseList #Create database 
collection = db.collection #Create collection within database

#Set up Chrome driver for web browsing
webdriver = "chromedriver.exe"
driver = Chrome(webdriver)



url = "https://online-learning.harvard.edu/catalog/free"
driver.get(url)

pages = driver.find_elements_by_xpath("//ul[@class='pager']/li[@class='pager-item']")
num_pages = len(pages)

course_list = []
for page in range(num_pages + 1):
	url = "https://online-learning.harvard.edu/catalog/Free?page=" + str(page)
	driver.get(url)
	courses = driver.find_elements_by_xpath("//ul[@class='course-grid']/li")
	for course in courses:
		course_title = course.find_element_by_class_name("field-name-title-qs").text
		course_topic = course.find_element_by_class_name("field-name-subject-area").text
		course_url = course.find_element_by_xpath("div/div/div/h3/a").get_attribute("href")
		course_object = {"name" : course_title, "topic" : course_topic, "platform" : "Harvard", "url" : course_url}
		course_list.append(course_object)

collection.insert_many(course_list)

driver.close()