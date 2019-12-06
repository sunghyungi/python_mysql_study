import pandas as pd

from Select.coffee_delete import delete_product
from Select.coffee_insert import insert_product, insert_products
from Select.coffee_select import query_with_fetchone, query_with_fetchall, query_with_fetchall2, query_with_fetchmany
from Select.coffee_update import update_product
from Select.connection_pool import ConnectionPool


def connection_pool_test():
    connect_pool = ConnectionPool.get_instance()
    connection = connect_pool.get_connection()
    print("connection : ", connection)


def fetchone():
    query_with_fetchone(sql)
    query_with_fetchone(sql2)


def fetchall():
    query_with_fetchall(sql)
    query_with_fetchall(sql2)


def fetchall2():
    res = query_with_fetchall2(sql)
    print(type(res), 'size = ', len(res))
    for pno, pname in res:
        print(pno, pname)
    res2 = query_with_fetchall2(sql2)
    print(type(res2), 'size = ', len(res2))
    for no, pno, price, count, margin in res2:
        print(no, pno, price, count, margin)


def insert1():
    query_with_fetchall(sql)
    insert_product(insert_sql, 'C001', '라떼')
    query_with_fetchall(sql)


if __name__ == "__main__":
    connection_pool_test()

    sql = "select * from product"
    sql2 = "select * from sale"
    #
    # fetchone()
    #
    # fetchall()
    #
    # fetchall2()
    #
    # query_with_fetchone("select * from product where code = '{}'".format('A001'))
    # query_with_fetchone("select * from sale where code = '{}'".format('A001'))
    # query_with_fetchmany(sql)

    # insert_sql = "insert into product values(%s, %s)"
    #
    # insert1()
    #
    # products = [('C002','라떼2'), ('C003','라떼3'),('C004','라떼4')]
    # insert_products(insert_sql, products)
    # query_with_fetchall(sql)

    # select_sql = "select code, name from product where code = '{}'".format('C001')
    # query_with_fetchone(select_sql)
    #
    # update_sql = "update product set name = %s where code = %s"
    # update_product(update_sql, '라떼수정', 'C001')
    #
    # query_with_fetchone(select_sql)

    select_sql = "select code, name from product where code like 'C___'"
    res = query_with_fetchall2(select_sql)
    columns_list = ['code', 'name']
    df = pd.DataFrame(res, columns=columns_list)
    print(df)

    delete_sql = "delete from product where code = %s"
    delete_product(delete_sql, 'C004')

    for code, name in (query_with_fetchall2(select_sql)):
        print(code, " ", name)
