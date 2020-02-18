


from selenium import webdriver
import time

def login(name, password ):

   
    # Start the driver/browser and open Url
    driver = webdriver.Chrome()
    driver.implicitly_wait(30)
    driver.get("https://twitter.com/login")

    # Get Telephone/username/e-mail field
    inputField = driver.find_element_by_name("session[username_or_email]")
    inputField.clear()
    inputField.send_keys(name)

    # Password
    inputField = driver.find_element_by_name("session[password]")
    inputField.clear()
    inputField.send_keys(password)
    time.sleep(3)

    # Login
    button = driver.find_element_by_xpath("//div[@role = 'button']/div/span/span")
    button.click()
    time.sleep(3)
    