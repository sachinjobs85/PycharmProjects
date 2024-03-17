from selenium import webdriver
from selenium.webdriver import Keys
import time

#driver = webdriver.Chrome()

# Username = "xyz"
# Password = "zxy"
driver = webdriver.Firefox()
url = 'https://lendlease.uat.ap.enablon.io/dashboard'

driver.get(url)

# driver.find_element_by_name("q").send_keys("Linkedin Login")
# driver.find_element_by_name("q").send_keys(Keys.ENTER)
# driver.find_element_by_partial_link_text("login").click()
driver.find_element_by_name("UserName").send_keys("UserName")
driver.find_element_by_name("Password").send_keys("pass")
driver.find_element_by_tag_name("button").click()
time.sleep(5)
print(driver.title)
print(driver.current_url)
driver.close()


