import pyodbc

server = 'sqlserver-rm88687.database.windows.net'
database = 'pythondb'
username = 'admsql'
password = 'devops@fiap22'
driver = '{ODBC Driver 17 for SQL Server}'


def db_query(command):
    with pyodbc.connect('DRIVER=' + driver + ';SERVER=' + server + ';PORT=1433;DATABASE=' + database + ';UID=' + username + ';PWD=' + password) as conn:
        with conn.cursor() as cursor:
            cursor.execute(command)
            row = cursor.fetchall()
            return row


def db_insert(command):
    with pyodbc.connect('DRIVER=' + driver + ';SERVER=' + server + ';PORT=1433;DATABASE=' + database + ';UID=' + username + ';PWD=' + password) as conn:
        with conn.cursor() as cursor:
            cursor.execute(command)
            conn.commit()
