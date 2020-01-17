# Class to send basic requests in order to
# create a new email account and perform tasks 
# on it.
# Responses are given to a parser to extract contents.
import requests


class HttpClient:

    def initial_request(self, url):
        # Initial request 
        response = requests.get(url)

        return response

    def send_request(self, url, session_cookies=None):
        # Send request
        response = requests.get(url, cookies=session_cookies)

        return response
