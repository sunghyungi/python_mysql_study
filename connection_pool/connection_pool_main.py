import inspect

from connection_pool.coneection_pool_study02 import ExplicitlyConnectionPool, get_implicitly_connection
from connection_pool.connection_pool_study import DatabaseConnectionPool


def connection_pool01():
    print("== {}() ==".format(inspect.stack()[0][3]))
    connection = DatabaseConnectionPool.get_instance().get_connection()
    print(type(connection), connection)
    connection.close()


def explicitly_connection_pool():
    print("== {}() ==".format(inspect.stack()[0][3]))
    connectionPool = ExplicitlyConnectionPool.get_instance()
    connection = connectionPool.get_connection()
    print(type(connection), connection)
    connection.close()


def implicitly_connection_pool():
    print("== {}() ==".format(inspect.stack()[0][3]))
    connectionPool = get_implicitly_connection()
    connection = connectionPool.get_connection()
    print(type(connection), connection)
    connection.close()


if __name__ == "__main__":
    # for i in range(20):
    #     connection_pool01()

    explicitly_connection_pool()
    implicitly_connection_pool()

    explicitly_connection_pool()
    implicitly_connection_pool()