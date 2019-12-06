from mysql.connector import Error

from Select.connection_pool import ConnectionPool


def insert_product(sql, code, name):
    args = (code, name)
    try:
        conn = ConnectionPool.get_instance().get_connection()
        cursor = conn.cursor()
        cursor.execute(sql, args)
        conn.commit()
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


def insert_products(sql, products):
    try:
        conn = ConnectionPool.get_instance().get_connection()
        cursor = conn.cursor()
        cursor.executemany(sql, products)
        conn.commit()
    except Error as e:
        print("Error:", e)
    finally:
        cursor.close()
        conn.close