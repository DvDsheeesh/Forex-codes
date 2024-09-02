import MetaTrader5 as mt5
import time
import pandas as pd

mt5.initialize()
#print(pd.DataFrame(mt5.copy_rates_from("EURUSD",mt5.TIMEFRAME_D1,datetime.datetime(2024,2,15),30)))

# print the positions
cn = 0
print()
for ggg in mt5.positions_get() :
    print(cn,"- buy /" if ggg.type == 0 else "sell /",ggg.symbol,"/",ggg.price_open,f"/ tp:{ggg.tp}",f"/ sl:{ggg.sl}")
    cn+=1
    print()

# choosing position number
posnum = int(input("which one ? : "))

# saving the desired position ticket so the code doesnt go to any other positions
postick = mt5.positions_get()[posnum].ticket

# far between bid/ask and sl
far = int(input(" far : "))

######################################################################################################################

# if position opened is sell
if mt5.positions_get()[posnum].type == 1 :

    # check when does the ask is far away from open price more than (far*2)
    while True :
        time.sleep(0.5)
        if mt5.symbol_info_tick(mt5.positions_get()[posnum].symbol).ask < mt5.positions_get()[posnum].price_open-(far/pow(10,mt5.symbol_info(mt5.positions_get()[posnum].symbol).digits)) :
            break

    # initializing value for sl
    slold = mt5.symbol_info_tick(mt5.positions_get()[posnum].symbol).ask + (far/pow(10,mt5.symbol_info(mt5.positions_get()[posnum].symbol).digits))
    
    # setting up the sl
    requestb = {
        "action": mt5.TRADE_ACTION_SLTP,
        "symbol": mt5.positions_get()[posnum].symbol,
        "sl": slold,
        "tp": mt5.positions_get()[posnum].tp,
        "position": postick,
    }
    aaa = mt5.order_send(requestb)
    print(aaa)

    # the new sl 
    slnew = 0

    # looping till position is closed
    while True :

        # giving the supposed new sl place
        slnew = mt5.symbol_info_tick(mt5.positions_get()[posnum].symbol).ask + (far/pow(10,mt5.symbol_info(mt5.positions_get()[posnum].symbol).digits))
        
        # comparing the new sl with old sl
        if slnew < slold :
            # if (new sl) is farest of the open price than (old sl) --> old sl = new sl
            slold = slnew
            # setting up the sl
            requestb = {
                "action": mt5.TRADE_ACTION_SLTP,
                "symbol": mt5.positions_get()[posnum].symbol,
                "sl": slold,
                "tp": mt5.positions_get()[posnum].tp,
                "position": postick,
            }
            aaa = mt5.order_send(requestb)

######################################################################################################################
######################################################################################################################
######################################################################################################################

if mt5.positions_get()[posnum].type == 0 :
    while True :
        if mt5.symbol_info_tick(mt5.positions_get()[posnum].symbol).bid > mt5.positions_get()[posnum].price_open+(far/pow(10,mt5.symbol_info(mt5.positions_get()[posnum].symbol).digits)) :
            print("hi")
            break

    slold = mt5.symbol_info_tick(mt5.positions_get()[posnum].symbol).bid - (far/pow(10,mt5.symbol_info(mt5.positions_get()[posnum].symbol).digits))
    requestb = {
        "action": mt5.TRADE_ACTION_SLTP,
        "symbol": mt5.positions_get()[posnum].symbol,
        "sl": slold,
        "tp": mt5.positions_get()[posnum].tp,
        "position": mt5.positions_get()[posnum].ticket,
    }
    aaa = mt5.order_send(requestb)
    slnew = 0
    
    while True :
        slnew = mt5.symbol_info_tick(mt5.positions_get()[posnum].symbol).bid - (far/pow(10,mt5.symbol_info(mt5.positions_get()[posnum].symbol).digits))
        if slnew > slold :
            slold = slnew
            requestb = {
                "action": mt5.TRADE_ACTION_SLTP,
                "symbol": mt5.positions_get()[posnum].symbol,
                "sl": slold,
                "tp": mt5.positions_get()[posnum].tp,
                "position": mt5.positions_get()[posnum].ticket,
            }
            aaa = mt5.order_send(requestb)
