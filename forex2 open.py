
import MetaTrader5 as mt5

# Initialize MetaTrader 5
mt5.initialize()
# Define the trade parameters
#symbol = "EURUSD"  # The symbol you want to trade
symbol = input(" symbol : ")
typp = int(input(" buy = 0 , sell = 1 : "))
lot_size = float(input(" lot_size : "))     # The lot size
typee = mt5.ORDER_TYPE_SELL if typp else mt5.ORDER_TYPE_BUY  # Order type: Sell/Buy
open_price = mt5.symbol_info_tick(symbol).bid if typp else mt5.symbol_info_tick(symbol).ask  # Current bid/ask price for the symbol
deviation = 20    # Maximum deviation from the requested price

# Send the trading request
request = {
    "action": mt5.TRADE_ACTION_DEAL,
    "symbol": symbol,
    "volume": lot_size,
    "type": typee,
    "price": open_price,
    "deviation": deviation,
    "magic": 0,
    "comment": "Python script open buy",
    "type_time": mt5.ORDER_TIME_GTC,
    "type_filling": mt5.ORDER_FILLING_IOC,
}

result = mt5.order_send(request)
if result.retcode == mt5.TRADE_RETCODE_DONE:
    print("Trade request executed successfully")
else:
    print("Trade request failed:", result.comment)

# Shut down MetaTrader 5
#mt5.shutdown()



"""
request = {
    "action": mt5.TRADE_ACTION_DEAL,
    "symbol": "EURUSD",
    "volume": 0.01,
    "type": mt5.ORDER_TYPE_BUY,
    "price": mt5.symbol_info_tick("EURUSD").ask,
    "sl": 0.0,
    "tp": 0.0,
    "deviation": 20,
    "type_time": mt5.ORDER_TIME_GTC,
    "type_filling": mt5.ORDER_FILLING_IOC,
}
result = mt5.order_send(request)
print(result)


"""