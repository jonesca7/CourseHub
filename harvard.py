from selenium.webdriver import Chrome

webdriver = "chromedriver.exe"
driver = Chrome(webdriver)

url = "https://online-learning.harvard.edu/catalog/free"
driver.get(url)

pages = driver.find_elements_by_xpath("//ul[@class='pager']/li[@class='pager-item']")
num_pages = len(pages)

for page in range(num_pages + 1):
	url = "https://online-learning.harvard.edu/catalog/Free?page=" + str(page)
	driver.get(url)
	courses = driver.find_elements_by_xpath("//ul[@class='course-grid']/li")
	for course in courses:
		course_title = course.find_element_by_class_name("field-name-title-qs").text
		course_topic = course.find_element_by_class_name("field-name-subject-area").text
		course_url = course.find_element_by_xpath("//h3/a").get_attribute("href")
		print(course_title + " " + course_topic + " " + course_url)