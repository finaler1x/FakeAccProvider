class FakeMailAddress:
    def __init__(self, address, cookies, inbox):
        self.address = address,
        self.cookies = cookies,
        self.inbox = inbox,


def get_address(self):
    return self.address


def set_address(self, address):
    self.address = address


def get_cookies(self):
    return self.cookies


def set_cookies(self, cookies):
    self.cookies = cookies


def get_inbox(self):
    return self.inbox


def set_inbox(self, inbox):
    self.inbox = inbox
