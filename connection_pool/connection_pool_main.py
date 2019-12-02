import inspect

from connection_pool.connection_pool_study import DatabaseConnectionPool


def connection_pool01():
    print("== {}() ==".format(inspect.stack()[0][3]))
    connection = DatabaseConnectionPool.get_instance().get_connection()
    print(type(connection), connection)
    connection.close()


if __name__ == "__main__":
    for i in range(20):
        connection_pool01()