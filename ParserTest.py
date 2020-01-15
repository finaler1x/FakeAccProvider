#Tests for ResponseParser class
#
#

from HttpClient import HttpClient 
from ResponseParser import ResponseParser


testUrl = "https://10minutemail.net/"

testClient = HttpClient()
testParser = ResponseParser()

# testResponse = testClient.initialRequest(testUrl)
# cookie = testParser.getCookies(testResponse)
cookie = {"PHPSESSID":"e2ee08ec196ed786ada381722fd1b5a5"}
testResponse = testClient.sendRequest(testUrl, cookie)
links = testParser.getInboxLinks(testResponse)

for link in links: 
    code = testParser.getTwitterCode(testClient.sendRequest(testUrl + link , cookie))
    print(code)
  
    
# Test getFakeAccData method
# print( testParser.getFakeAccData(testResponse))

#Test getInboxLinks method
# print( testParser.getInboxLinks(testResponse))

#Test ... method
#  print()



