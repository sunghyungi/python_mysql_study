from mysql.connector import Error

from Select.connection_pool import ConnectionPool


def query_with_fetchone(sql):
    try:
        conn = ConnectionPool.get_instance().get_connection()
        cursor = conn.cursor()
        cursor.execute(sql)
        row = cursor.fetchone()
        while row is not None:
            print(type(row), ":", row)
            row = cursor.fetchone()
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


def query_with_fetchall(sql):
    try:
        conn = ConnectionPool.get_instance().get_connection()
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        print('Total Row(s):', cursor.rowcount)
        for row in rows:
            print(type(row), " ", row)
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


def query_with_fetchall2(sql):
    try:
        conn = ConnectionPool.get_instance().get_connection()
        cursor = conn.cursor()
        cursor.execute(sql)
        return cursor.fetchall()
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


def iter_row(cursor, size = 5):
    while True:
        rows = cursor.fetchmany(size)
        if not rows:
            break
        for row in rows:
            yield row



def query_with_fetchmany(sql):
    try:
        conn = ConnectionPool.get_instance().get_connection()
        cursor = conn.cursor()
        cursor.execute(sql)
        for row in iter_row(cursor, 5):
            print(type(row), " ", row)
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

