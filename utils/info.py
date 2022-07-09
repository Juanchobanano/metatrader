import MetaTrader5 as mt5

def get_account_info():
    # Obtiene la información sobre la cuenta comercial actual
    data = mt5.account_info()
    #print(help(data))
    data = {
        "assets": data.assets, 
        "balance": data.balance, 
        "commission_blocked": data.commission_blocked, 
        "company": data.company, 
        "credit": data.credit, 
        "currency": data.currency, 
        "currency_digits": data.currency_digits, 
        "equity": data.equity, 
        "fifo_close": data.fifo_close, 
        "leverage": data.leverage, 
        "liabilities": data.liabilities, 
        "limit_orderes": data.limit_orders, 
        "login": data.login, 
        "margin": data.margin, 
        "margin_free": data.margin_free, 
        "margin_initial": data.margin_initial, 
        "margin_level": data.margin_level, 
        "margin_maintenance": data.margin_maintenance, 
        "margin_mode": data.margin_mode, 
        "margin_so_call": data.margin_so_call,
        "margin_so_mode": data.margin_so_mode, 
        "magin_so_so": data.margin_so_so, 
        "name": data.name, 
        "profit": data.profit, 
        "server": data.server,
        "trade_allowed": data.trade_allowed, 
        "trade_expert": data.trade_expert, 
        "trade_mode": data.trade_mode
    }
    print(data)


def get_info():
    """DOCS: https://www.mql5.com/es/docs/integration/python_metatrader5
    """

    # Retorna la versión del terminal MetaTrader 5
    print(mt5.version())

    # Obtiene el estado y los parámetros del terminal MetaTrader 5 conectado
    print(mt5.terminal_info())

    # Obtiene el número de órdenes activas.
    print(mt5.orders_total())

    # Obtiene el número de posiciones abiertas
    print(mt5.positions_total())

    # Obtiene el número de órdenes en la historia comercial en el intervalo indicado
    print(mt5.history_orders_total())

    # Obtiene el número de transacciones en la historia comercial en el intervalo indicado
    print(mt5.history_deals_total())

    # Retorna el tamaño del margen en la divisa de la cuenta para realizar la operación comercial indicada
    print(mt5.order_calc_margin())

    # Retorna el tamaño del beneficio en la divisa de la cuenta para la operación comercial indicada
    print(mt5.order_calc_profit())

    # Obtiene el número de transacciones en la historia comercial en el intervalo indicado
    print(mt5.history_deals_get())