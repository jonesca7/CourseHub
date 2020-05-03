from selenium.webdriver import Chrome
from pymongo import MongoClient

db_client = MongoClient('mongodb+srv://jonesca7:tohacks2020@coursehub-8qtyk.gcp.mongodb.net/test?retryWrites=true&w=majority')
db = db_client.CourseList #Create database 
collection = db.collection #Create collection

webdriver = "chromedriver.exe"
driver = Chrome(webdriver)

url = "https://online.stanford.edu/search-catalog?free_or_paid%5Bfree%5D=free&type=All"
driver.get(url)

pages = driver.find_elements_by_xpath("//li[@class='pager__item']")
num_pages = len(pages)

course_list = []
for page in range(num_pages + 1):
	url = "https://online.stanford.edu/search-catalog?free_or_paid%5Bfree%5D=free&type=All&page=" + str(page)
	driver.get(url)
	courses = driver.find_elements_by_xpath("//div[@class='search-results--table']/a")
	for course in courses:
		course_title = course.find_element_by_xpath("div/h3").text
		course_topic = course.find_element_by_xpath("div/h4").text.partition(" of ")[2]
		course_url = course.get_attribute("href")
		course_object = {"name" : course_title, "topic" : course_topic, "platform" : "Stanford University", "url" : course_url}
		print(course_topic)
		course_list.append(course_object)

collection.insert_many(course_list)

driver.close()