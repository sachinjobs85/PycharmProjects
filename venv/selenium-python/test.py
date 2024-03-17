# import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By

# create webdriver object
driver = webdriver.Firefox()

# get geeksforgeeks.org
driver.get("https://lendlease.uat.ap.enablon.io/dashboard")

# get element
#element = driver.find_element(By.ID, "gsc-i-id1")

# send keys
#element.send_keys("Arrays")

username = driver.find_element(By.NAME, 'Username')
password = driver.find_element(By.NAME, 'Password')

username.send_keys("yourUsername") #type your own username here
password.send_keys("yourPassword") #type your own password here

driver.find_element(By.NAME, 'Sign In').click()
