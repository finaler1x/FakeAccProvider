# DatabaseConnectorTest
# Test SSH and MySql-Connection

from DatabaseConnector import DatabaseConnector

# test data
test_account_data = {
    "name": "Maxi Musti",
    "address": "Berlinerstr 1",
    "password": "supersecurepw123",
    "created": "4:20:2040",
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
