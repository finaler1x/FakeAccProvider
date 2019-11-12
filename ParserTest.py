#Tests for ResponseParser class
#
#

from HttpClient import HttpClient 
from ResponseParser import ResponseParser


testUrl = "https://10minutemail.net/"

testClient = HttpClient()
testParser = ResponseParser()

testResponse = testClient.initialRequest(testUrl)

#Test getFakeAccData method
print( testParser.getFakeAccData(testResponse))

#Test getInboxLinks method
print( testParser.getInboxLinks(testResponse))

#Test ... method
# print()



