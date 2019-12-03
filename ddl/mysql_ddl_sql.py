from mysql.connector import Error, errorcode

from connection_pool.coneection_pool_study02 import ExplicitlyConnectionPool

DB_NAME = 'coffee'
TABLES = {'product': (
    """
    CREATE TABLE product(
    code CHAR(4) NOT NULL,
    name VARCHAR(2) null,
    primary key (code))
    """
), 'sale': (
    """
    CREATE TABLE sale (
    no INT(11) auto increment,
    code CHAR(4) NOT NULL,
    price INT(11) NOT NULL,
    saleCnt INT(11) NOT NULL,
    marginRate INT(11) NOT NULL,
    primary key (no),
    FOREIGN KEY (code) references product (code))
    """
)}


def create_database():
    try:
        conn = ExplicitlyConnectionPool.get_instance().get_connection()
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
        print("CREATE DATABASE {}".format(DB_NAME))
    except Error as err:
        if err.errno == errorcode.ER_DB_CREATE_EXISTS:
            cursor.execute("DROP DATABASE {}".format(DB_NAME))
            print("DROP DATABASE {}".format(DB_NAME))
            cursor.execute("CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
        else:
            print(err.msg)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()


def create_table():
    try:
        conn = ExplicitlyConnectionPool.get_instance().get_connection()
        cursor = conn.cursor()
        cursor.execute("USE {}".format(DB_NAME))
        for table_name in TABLES:
            table_description = TABLES[table_name]
            print('table_description', table_description)
            try:
                print("Creating table{}: ".format(table_name), end='')
                cursor.execute(table_description)
            except Error as err:
                if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                    print("already exists.")
                else:
                    print(err.msg)
            else:
                print("OK")
    except Error as err:
        print(err)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()


if __name__ == "__main__":
    create_database()
    create_table()