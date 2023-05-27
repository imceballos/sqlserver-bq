import os
import sqlalchemy

def connect_tcp_socket():
    """ Initializes a TCP connection pool for a SQL Server instance. """
    db_host = '127.0.0.1'  # e.g., '127.0.0.1' ('172.17.0.1' if deployed to GAE Flex)
    db_user =  # e.g., 'my-db-user'
    db_pass =  # e.g., 'my-db-password'
    db_name =  # e.g., 'my-database'
    db_port =  # e.g., 1433

    driver = 'ODBC Driver 17 for SQL Server'  # Specify the appropriate driver name

    # Set the driver name in the connection string
    connection_string = f"mssql+pyodbc://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}?driver={driver}"

    # Create the engine with the modified connection string
    pool = sqlalchemy.create_engine(connection_string)
    print("pase aca")
    with pool.connect() as connection:
        # Execute SQL queries
        print("hello")
        query = sqlalchemy.text("SELECT name FROM master.sys.databases")  # Use text() to create an executable query object
        result = connection.execute(query)
        for row in result:
            print(row)

connect_tcp_socket()
#connection = pool.connect()
#result = connection.execute("SELECT * FROM your_table")
#for row in result:
#    print(row)