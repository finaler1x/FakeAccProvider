# Script to test the creation of an account on
# Instagramm. Extends the InstaRegisterStepTest by
# saving the data to a file.
# The goal is to create a new account and confirm it
# with the activation link sent by Instagramm




from HttpClient import HttpClient 
from ResponseParser import ResponseParser
import InstaRegisterStep
import json


testUrl = "https://10minutemail.net/"

testClient = HttpClient()
testParser = ResponseParser()

testResponse = testClient.initialRequest(testUrl)

# Get mail adress
testAcc = testParser.getFakeAccData(testResponse)

# Save sessionCookies to file for now
testFile = open("test.txt","w+")
testFile.write(json.dumps(testAcc[1]))
testFile.close()

# Call InstaRegisterStep
InstaRegisterStep.register(testAcc[0], "Bernd Bot", "BerndBot", "BerndBotPassword")