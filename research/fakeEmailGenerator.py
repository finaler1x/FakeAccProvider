from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pickle

driver = webdriver.Chrome()

driver.get("https://www.tempmailaddress.com/")

# searchBox = driver.find_elements_by_id("mail")
# fakeEmailAddress = searchBox.send_keys(Keys.CONTROL, 'c')

element = driver.find_element_by_id("email")
element["text"]

print(element)


driver.close