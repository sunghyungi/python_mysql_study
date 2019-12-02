from mysql.connector import Error, MySQLConnection

try:
    conn = MySQLConnection(host="localhost",
                           database="mysql",
                           user="root",
                           password="rootroot")
    print(conn)
except Error as e:
    print(e)
