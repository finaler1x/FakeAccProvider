# DatabaseConnectorTest
# Test SSH and MySql-Connection

from Sql.DatabaseConnector import DatabaseConnector
import datetime

# test data
test_account_data = {
    "name": "bsinfo_fan",
    "address": "",
    "password": "supersecurepw",
    "created": str(datetime.datetime.now()),
}

# Test creating connection
sql_connector = DatabaseConnector()
connection = sql_connector.init_sql_connection()

# Test select query
sql_connector.read_account_data(connection)

# Test insert query
sql_connector.add_account_data(connection, test_account_data)

# Test close function
sql_connector.close_connection(connection)
