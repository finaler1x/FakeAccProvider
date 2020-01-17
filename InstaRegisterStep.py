# Script for the register page of Instagramm
# URL : https://www.instagram.com

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def register(email_adr, full_name, user_name, password):
    # Start the driver/browser and open Url
    driver = webdriver.Chrome()
    driver.implicitly_wait(30)
    driver.get("https://www.instagram.com")

    # Email
    input_field = driver.find_element_by_name("emailOrPhone")
    input_field.clear()
    input_field.send_keys(email_adr)

    # Name
    input_field = driver.find_element_by_name("fullName")
    input_field.clear()
    input_field.send_keys(full_name)

    # Username
    input_field = driver.find_element_by_name("username")
    input_field.clear()
    input_field.send_keys(user_name)

    # Password
    input_field = driver.find_element_by_name("password")
    input_field.clear()
    input_field.send_keys(password)

    # Send/Submit
    button = driver.find_element_by_xpath("//button[@type='submit']").click()
