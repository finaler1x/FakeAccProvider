from sshtunnel import SSHTunnelForwarder
import mysql.connector


class DatabaseConnector:

    def init_sql_connection(self):
        with SSHTunnelForwarder(
                ('localhost', 2222),
                ssh_username="vagrant",
                ssh_password="vagrant",
                remote_bind_address=('127.0.0.1', 3306),
                # local_bind_address=('0.0.0.0', 10022)
        ) as connection:
            db_connection = mysql.connector.connect(
                host="127.0.0.1",
                user="remote",
                password="remote",
                # database="fake_account_db"
            )

            return db_connection

    def add_account_data(self, db_connection, account_data):
        sql = """INSERT INTO fake_account_db.fake_accounts (Name, Address, Password, Created) VALUES (%s, %s, %s, %s)"""

        # Extract row data
        name = account_data.get("name")
        address = account_data.get("address")
        password = account_data.get("password")
        created = account_data.get("created")

        values = (name, address, password, created)

        cursor = db_connection.cursor()
        cursor.execute(sql, values)

        db_connection.commit()
        cursor.close()

    def read_account_data(self, db_connection):
        sql = "SELECT * FROM fake_account_db.fake_accounts"

        # Handle values and execute sql query
        cursor = db_connection.cursor()
        cursor.execute(sql)

        # Get all data from table
        result = cursor.fetchall()

        cursor.close()

        return result

    def close_connection(self, db_connection):
        db_connection.close()
