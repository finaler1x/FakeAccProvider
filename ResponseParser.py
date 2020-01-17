# Handles http responses and parses for 
# requested data.
# This parser is currently only able to handle responses 
# from "https://10minutemail.net/".
# 
import re
from bs4 import BeautifulSoup as bso


class ResponseParser:

    # Returns the data needed by a FakeMailAccount Object
    def get_fake_acc_data(self, response):
        beautiful_content = bso(response.content, "html.parser")

        mail_address = self.get_mail_adress(beautiful_content)
        cookies = self.get_cookies(response)

        return mail_address, cookies

    # Get the e-mail adress of the fake account
    def get_mail_adress(self, content):
        input_element = content.find("input")
        mail_address = input_element.get("value")

        return mail_address

    # Return all cookies as a dictionary: ["key":"value",...]
    def get_cookies(self, response):
        session_cookies = response.cookies.get_dict()

        return session_cookies

    # Return a list of the link endings for the mails 
    def get_inbox_links(self, response):
        beautiful_content = bso(response.content, "html.parser")
        inbox_elements = beautiful_content.find("table")
        trimmed_links = []

        for mails in inbox_elements.contents:
            link = mails.attrs.get('onclick')
            if link:
                extracted_link = re.findall("readmail.html.*'", link)
                trimmed_links.append(extracted_link[0].strip("'"))

        return trimmed_links

    def get_fake_name(self, response):
        response_data = response.json()

        name = response_data['name']
        surname = response_data['surname']
        password = response_data['password']

        name += surname

        return {
            "name": name,
            "password": password
        }

    # Get the validation code for twitter
    def get_twitter_code(self, response):
        beautiful_content = bso(response.content, "html.parser")
        codes = beautiful_content.findAll("td", attrs={"class": "h1 black", "dir": "ltr"})
        for code in codes:
            code = code.getText()
            if code.isnumeric():
                return code
            else:
                return -1
