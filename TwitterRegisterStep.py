# Script for the register page of twitter
# URL : https://www.twitter.com
# 
#  
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import json
from HttpClient import HttpClient
from ResponseParser import ResponseParser


def register(mail_account, name, password):
    # Set up
    mail_url = "https://10minutemail.net/"
    http_client = HttpClient()
    http_parser = ResponseParser()

    # Start the driver/browser and open Url
    driver = webdriver.Chrome()
    driver.implicitly_wait(30)
    driver.get("https://twitter.com/i/flow/signup")

    # Switch from phone number to email
    driver.find_element_by_xpath("//div[@role = 'button']/span").click()

    # Name
    input_field = driver.find_element_by_name("name")
    input_field.clear()
    input_field.send_keys(name)

    # Mail
    input_field = driver.find_element_by_name("email")
    input_field.clear()
    input_field.send_keys(mail_account[0])
    time.sleep(3)

    # Go to next page
    button = driver.find_element_by_xpath("//div[@role = 'button']/div/span/span")
    button.click()

    # Tick checkboxes
    # button = driver.find_elements_by_xpath("//input[@type ='checkbox']")[0]
    # button.click()
    button = driver.find_elements_by_xpath("//input[@type ='checkbox']")[1]
    button.click()
    # button = driver.find_elements_by_xpath("//input[@type ='checkbox']")[2]
    # button.click()

    # Go to next page
    button = driver.find_element_by_xpath("//div[@role = 'button']/div/span/span")
    button.click()

    # Register
    button = driver.find_element_by_xpath("//div[@role = 'button']/div/span/span")
    button.click()

    # Get the verification code
    links = http_parser.get_inbox_links(http_client.send_request(mail_url, mail_account[1]))
    while len(links) < 2:
        links = http_parser.get_inbox_links(http_client.send_request(mail_url, mail_account[1]))
        time.sleep(10)

    code = http_parser.get_twitter_code(http_client.send_request(mail_url + links[0], mail_account[1]))

    # Write the code
    input_field = driver.find_element_by_name("verfication_code")
    input_field.clear()
    input_field.send_keys(code)
    time.sleep(3)

    # Go to next page
    button = driver.find_element_by_xpath("//div[@role = 'button']/div/span/span")
    button.click()

    # Select a password
    input_field = driver.find_element_by_name("password")
    input_field.clear()
    input_field.send_keys(password)
    time.sleep(3)

    # Go to next page
    button = driver.find_element_by_xpath("//div[@role = 'button']/div/span/span")
    button.click()
    time.sleep(3)

    # Skip selecting a picture
    button = driver.find_element_by_xpath("//div[@role = 'button']/div/span/span")
    button.click()
    time.sleep(1)

    # Skip the biography
    button = driver.find_element_by_xpath("//div[@role = 'button']/div/span/span")
    button.click()
    time.sleep(2)

    # Skip interests
    button = driver.find_element_by_xpath("//div[@role = 'button']/div/span/span")
    button.click()
    time.sleep(3)

    # Skip following
    button = driver.find_element_by_xpath("//div[@role = 'button']/div/span/span")
    button.click()
    time.sleep(2)

    # Allow notifications
    buttons = driver.find_elements_by_xpath("//div[@role = 'button']/div/span/span")
    buttons[1].click()
    time.sleep(2)

    # Close getting started
    button = driver.find_element_by_xpath("//div[@aria-label = 'Close']")
    button.click()
    time.sleep(2)
