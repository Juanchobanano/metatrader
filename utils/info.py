import MetaTrader5 as mt5

def get_info():
    """DOCS: https://www.mql5.com/es/docs/integration/python_metatrader5
    """
    print(mt5.version())
    print(mt5.terminal_info())
    print(mt5.account_info())
    print(mt5.orders_total())
    print(mt5.positions_total())
    print(mt5.history_orders_total())
    print(mt5.history_deals_total())
    print(mt5.order_calc_margin())
    print(mt5.order_calc_profit())