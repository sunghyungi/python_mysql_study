from transaction.coffee_procedure import call_sale_stat_sp, call_order_price_by_issale
from transaction.create_procedure import create_procedure
from transaction.transaction_query import transaction_fail1, transaction_fail2, transaction_fail3

if __name__ == "__main__":
    # transaction_fail1()
    # transaction_fail2()
    # transaction_fail3()
    # create_procedure()
    call_sale_stat_sp('proc_sale_stat')
    print()
    call_order_price_by_issale('proc_saledetail_orderby', False)
    print()
    call_order_price_by_issale('proc_saledetail_orderby', True)