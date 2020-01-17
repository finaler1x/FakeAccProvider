# Script to test the creation of an account on
# Instagramm. Extends the InstaRegisterStepTest by
# saving the data to a file.
# The goal is to create a new account and confirm it
# with the activation link sent by Instagramm

from HttpClient import HttpClient 
from ResponseParser import ResponseParser
import TwitterRegisterStep
import json


test_url = "https://10minutemail.net/"
fake_name_api_url = "https://uinames.com/api/?ext&region=united+states"

test_client = HttpClient()
test_parser = ResponseParser()

test_response = test_client.initial_request(test_url)
testNameResponse = test_client.send_request(fake_name_api_url)

# Get mail address
test_acc = test_parser.get_fake_acc_data(test_response)

# Get fake name
testNameData = test_parser.get_fake_name(testNameResponse)

# Save sessionCookies to file for now
testFile = open("test.txt","w+")
testFile.write(json.dumps(test_acc[1]))
testFile.close()

# Call TwitterRegisterStep
# TwitterRegisterStep.register(testAcc[0], "Bernd Bot", "BerndBot", "BerndBotPassword")
TwitterRegisterStep.register(test_acc, "Bernd Bot", "BerndBotPassword")