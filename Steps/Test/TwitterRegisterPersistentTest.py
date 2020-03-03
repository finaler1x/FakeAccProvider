# Create a new twitter account and save it in db.
# 21.02.2020
from Sql import DatabaseConnector
from Steps import TwitterRegisterStep
from HTTP import HttpClient
from Parser import ResponseParser
import datetime

# Initial config
username = 'bsinfo_fan'
user_password = 'supersecurepw'
# Get mail account
mailUrl = "https://10minutemail.net/"

testClient = HttpClient.HttpClient()
testParser = ResponseParser.ResponseParser()

mailResponse = testClient.initialRequest(mailUrl)
mailAccount = testParser.getFakeAccData(mailResponse)

# Register at twitter
TwitterRegisterStep.register(mailAccount, username, user_password)

# Add account to db

account_data = {
    "name": username,
    "address": mailAccount[0],
    "password": user_password,
    "created": str(datetime.datetime.now()),
}
connector = DatabaseConnector.DatabaseConnector()
connection = connector.init_sql_connection()
connector.add_account_data(connection, account_data)
connector.close_connection(connection)
