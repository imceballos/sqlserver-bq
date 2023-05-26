from dotenv import load_dotenv
import logging
import pyodbc
import os

load_dotenv()


class SQLServer:
    def __init__(self):
        self.driver_name = os.getenv("DRIVER_NAME")
        self.server_name = os.getenv("SERVER_NAME")
        self.sql_user = os.getenv("SQL_USER")
        self.sql_pass = os.getenv("SQL_PASS")
        self.conn = None

    def connect_to_server(self):
        try:
            self.conn = pyodbc.connect(self._connection_string())
            logging.info("Connection stablished")
        except Exception as e:
            logging.error(str(e))
        return self.conn

    def _connection_string(self):
        return f"""
          DRIVER={{{self.driver_name}}};
          SERVER={self.server_name};
          UID={self.sql_user};
          PWD={self.sql_pass};
          """

    def query(self, sql_statement):
        if self.conn is None:
            logging.error("Connection is absent")
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql_statement)
            data = cursor.fetchall()
            columns = [col[0] for col in cursor.description]
            return columns, data
        except Exception as e:
            logging.error(str(e))


#server = SQLServer()
#server.connect_to_server()


import pyodbc
CONNECTION_STRING = f"DRIVER={{{os.getenv('DRIVER_NAME')}}};SERVER={os.getenv('SERVER_NAME')};UID={os.getenv('SQL_USER')};PWD=thisismynewpassword"

database = "testdb"
with pyodbc.connect(CONNECTION_STRING, autocommit=True).cursor() as cursor:
    cursor.execute(f"DROP DATABASE IF EXISTS {database}")
    cursor.execute(f"CREATE DATABASE {database}")

    # Print the list of databases in the instance, showing that testdb has been created.
    cursor.execute("SELECT name FROM master.sys.databases")
    for row in cursor:
        db_name = row[0]
        print(db_name + (" <<--- CREATED" if db_name == database else ""))