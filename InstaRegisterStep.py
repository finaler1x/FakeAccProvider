# Script for the register page of Instagramm
# URL : https://www.instagram.com
# 
#  

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def register(emailAdr, fullName, userName, password ):

    # Start the driver/browser and open Url
    driver = webdriver.Chrome()
    driver.implicitly_wait(30)
    driver.get("https://www.instagram.com")
    
    # Email
    inputField = driver.find_element_by_name("emailOrPhone")
    inputField.clear()
    inputField.send_keys(emailAdr)    

    # Name
    inputField = driver.find_element_by_name("fullName")
    inputField.clear()
    inputField.send_keys(fullName)

    # Username
    inputField = driver.find_element_by_name("username")
    inputField.clear()
    inputField.send_keys(userName)

    # Password
    inputField = driver.find_element_by_name("password")
    inputField.clear()
    inputField.send_keys(password)

    # Send/Submit
    button = driver.find_element_by_xpath("//button[@type='submit']").click()
    
   
    

