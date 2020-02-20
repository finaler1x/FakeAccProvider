from datetime import date

from sshtunnel import SSHTunnelForwarder
import mysql.connector


class DatabaseConnector:

    def init_sql_connection(self):

        try:
            with SSHTunnelForwarder(
                    ('localhost', 2222),
                    ssh_username="vagrant",
                    ssh_password="vagrant",
                    remote_bind_address=('127.0.0.1', 3306),
            ) as connection:
                db_connection = mysql.connector.connect(
                    host="127.0.0.1",
                    user="remote",
                    password="remote",
                )

        except mysql.connector.Error as error:
            print("Failed to connect: {}".format(error))
        finally:
            return db_connection

    def add_account_data(self, db_connection, account_data):

        cursor = None
        sql = """INSERT INTO fake_account_db.fake_accounts (Name, Address, Password, Created) VALUES (%s, %s, %s, %s)"""

        # Extract row data
        name = account_data.get("name")
        address = account_data.get("address")
        password = account_data.get("password")
        created = account_data.get("created")

        values = (name, address, password, created)

        try:
            cursor = db_connection.cursor()
            cursor.execute(sql, values)
        except mysql.connector.Error as error:
            print("Failed to add data: {}".format(error))
        finally:
            db_connection.commit()
            cursor.close()

    def read_all_data(self, db_connection):

        cursor = None
        result = None
        sql = "SELECT * FROM fake_account_db.fake_accounts"

        try:
            # Handle values and execute sql query
            cursor = db_connection.cursor()
            cursor.execute(sql)

            # Get all data from cursor
            result = cursor.fetchall()
        except mysql.connector.Error as error:
            print("Failed to read data: {}".format(error))
        finally:
            cursor.close()

        return result

    def read_account_data_by_data(self, db_connection, input):

        cursor = None
        result = None
        sql = """SELECT * FROM fake_account_db.fake_accounts WHERE Created = %s """

        # Rewrite input if with actual data if today
        if input == "today":
            value = date.today()
        else:
            value = input

        try:
            cursor = db_connection.cursor()
            cursor.execute(sql, value)
        except mysql.connector.Error as error:
            print("Failed to read data by date: {}".format(error))
        finally:
            db_connection.commit()
            cursor.close()

    def delete_account_data_by_date(self, db_connection, value):

        cursor = None
        result = None
        sql = """DELETE * FROM fake_account_db.fake_accounts WHERE Created = %s"""

        # Rewrite input if with actual data if today
        if input == "today":
            value = date.today()
        else:
            value = input

        try:
            cursor = db_connection.cursor()
            cursor.execute(sql, value)
        except mysql.connector.Error as error:
            print("Failed to read data: {}".format(error))
        finally:
            cursor.close()

    def close_connection(self, db_connection):
        db_connection.close()
