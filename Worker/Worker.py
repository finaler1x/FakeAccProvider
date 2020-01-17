from config import *
from HttpClient import HttpClient
from FakeMailAccount import FakeMailAddress

# Worker creates client instance depending on config
# and fills client responses to FakeAccount instances
# Params: 
#   client HttpClient
#   account FakeMailAccount
class Worker:
    client = None,
    account = None

# Creates an instance of HttpClient
# Params: url str
def createClient(self, url):
    return HttpClient(url)

def getClient(self):
    return self.client

def setClient(self, client):
    self.client = client

# Creates an instance of FakeAccount
# Params: Address, Cookies, Inbox
def createFakeMailAccount(self, address, cookies, inbox):
    return FakeMailAddress(address, cookies, inbox)

def getFakeMailAccount(self):
    return self.account

def setFakeMailAccount(self, account):
    self.account = account

