# Handles http responses and parses for 
# requested data.
# This parser is currently only able to handle responses 
# from "https://10minutemail.net/".
# 
import re
from bs4 import BeautifulSoup as bso

class ResponseParser():

    # Returns the data needed by a FakeMailAccount Object
    def getFakeAccData(self, response):               
            beautifulContent = bso(response.content, "html.parser")
            
            mailAdress = self.getMailAdress(beautifulContent)
            cookies = self.getCookies(response)

            return mailAdress, cookies
        

    # Get the e-mail adress of the fake account
    def getMailAdress(self, content):
            inputElement = content.find("input")
            mailAdress   = inputElement.get("value")

            return mailAdress


    # Return all cookies as a dictionary: ["key":"value",...]
    def getCookies(self, response):
            sessionCookies = response.cookies.get_dict()
    
            return sessionCookies


    # Return a list of the link endings for the mails 
    def getInboxLinks(self, response):
            beautifulContent = bso(response.content, "html.parser")
            inboxElements = beautifulContent.find("table")
            trimmedLinks = []
            
            for mails in inboxElements.contents:
                link = mails.attrs.get('onclick')
                if (link):
                    extractedLink = re.findall("readmail.html.*'", link)
                    trimmedLinks.append(extractedLink[0].strip("'"))
            return trimmedLinks

