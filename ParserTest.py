# Tests for ResponseParser class
#
#

from HttpClient import HttpClient
from ResponseParser import ResponseParser

test_url = "https://10minutemail.net/"

test_client = HttpClient()
test_parser = ResponseParser()

# testResponse = testClient.initialRequest(testUrl)
# cookie = testParser.getCookies(testResponse)
cookie = {"PHPSESSID": "e2ee08ec196ed786ada381722fd1b5a5"}
test_response = test_client.send_request(test_url, cookie)
links = test_parser.get_inbox_links(test_response)

for link in links:
    code = test_parser.get_twitter_code(test_client.send_request(test_url + link, cookie))
    print(code)

# Test getFakeAccData method
# print( testParser.getFakeAccData(testResponse))

# Test getInboxLinks method
# print( testParser.getInboxLinks(testResponse))

# Test ... method
#  print()
