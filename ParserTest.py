# Tests for ResponseParser class

from HttpClient import HttpClient 
from ResponseParser import ResponseParser


test_url = "https://10minutemail.net/"

test_client = HttpClient()
test_parser = ResponseParser()

test_response = test_client.initial_request(test_url)

# Test getFakeAccData method
print(test_parser.get_fake_acc_data(test_response))

# Test getInboxLinks method
print(test_parser.get_inbox_links(test_response))

# Test ... method
# print()



