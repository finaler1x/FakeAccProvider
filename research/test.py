from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests

driver = webdriver.Chrome()

driver.get("https://www.google.de")
assert "Google" in driver.title

# Navigate google and query
searchBox = driver.find_element_by_name("q")
searchBox.clear
searchBox.send_keys("bsinfo")
searchBox.submit()
