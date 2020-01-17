# Class to send basic requests in order to
# create a new email account and perform tasks 
# on it.
# Responses are given to a parser to extract contents.
import requests


class HttpClient():
        
    def initialRequest(self, url):
        # Initial request 
        response = requests.get(url)

        return response

    def sendRequest(self, url, sessionCookies):
        # Send request
        response = requests.get(url, cookies=sessionCookies)

        return response

    
        

    

    
