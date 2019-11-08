import requests
import re
from bs4 import BeautifulSoup as bso

testCookie = {'PHPSESSID': 'f1720ee65ea1bddd48a9f7482e64479f'} 

class HttpClient():
    def __init__(self, startUrl):
        self.url = startUrl
        self.response = self.sendRequest(startUrl),
        self.content  = self.getParsedResponseContent(self.response),
        self.email    = self.getMailAdress(self.content),
        self.cookies  = self.getCookies(self.response),
        self.inbox    = self.getInbox(self.content)

    def sendRequest(self, startUrl):
        # Remove test cookie when tested
        response = requests.get(startUrl, cookies=testCookie)

        return response

    def getParsedResponseContent(self, response):
        content = response[0].content
        soupContent = bso(content, "html.parser")

        return soupContent

    def getMailAdress(self, content):
        inputElement = content[0].find("input")
        inputValue   = inputElement.get("value")

        return inputValue
        
    def getCookies(self, response):
        sessionCookies = response[0].cookies.get_dict()
       

        return sessionCookies

    def extendAccountLifeSpan(self, extenderUrl):
        requests.get(extenderUrl, cookies=self.cookies[0])
        

    def getInbox(self, content):
        inboxElements = content[0].find("table")

        trimmedLinks = []

        for mails in inboxElements.contents:

            link = mails.attrs.get('onclick')

            if (link):
                extractedLink = re.findall("readmail.html.*'", link)
                trimmedLinks.append(extractedLink[0].strip("'"))

        return trimmedLinks

    def openMails(self):
        inbox = self.getInbox(self.content)
        for link in inbox:
            mail = requests.get(self.url + '/' + link, cookies = self.cookies[0])
            print (mail.text)
