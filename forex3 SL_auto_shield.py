# this python script is made to implement an auto moving SL on your opened position 
# it asks you to enter the number of wanted TPs then it automatically creates values for TP and it moves the SL along with the moving of the indicator
# every tp is reached, the SL is moved to the past TP

import MetaTrader5 as mt5 
import time
import pandas as pd

mt5.initialize()

# print the positions
cn = 0
print()
for ggg in mt5.positions_get() :
    print(cn,"- buy /" if ggg.type == 0 else "sell /",ggg.symbol,"/",ggg.price_open,f"/ tp:{ggg.tp}",f"/ sl:{ggg.sl}")
    cn+=1
    print()

# choosing position number
posnum = int(input("which one ? : "))

# saving the desired position so the code doesnt go to any other positions
pos = mt5.positions_get()[posnum]

tpcount = int(input(" how many tp ? : "))

last_tp = mt5.positions_get()[posnum].tp

tpar = [mt5.positions_get()[posnum].price_open]

rangee = (last_tp - mt5.positions_get()[posnum].price_open if mt5.positions_get()[posnum].type == 0 else mt5.positions_get()[posnum].price_open - last_tp)

for i in range(1,tpcount):
    tpar.append(mt5.positions_get()[posnum].price_open + i * rangee / tpcount if mt5.positions_get()[posnum].type == 0 else mt5.positions_get()[posnum].price_open - i * rangee / tpcount)

print(tpar)

for numtp in range(tpcount):
    # if position opened is buy
    if mt5.positions_get()[posnum].type == 0 :
        
        while mt5.symbol_info_tick(mt5.positions_get()[posnum].symbol).bid < tpar[numtp+1] :
            time.sleep(0.2)
            continue
        requestb = {
            "action": mt5.TRADE_ACTION_SLTP,
            "symbol": mt5.positions_get()[posnum].symbol,
            "sl": tpar[numtp],
            "tp": mt5.positions_get()[posnum].tp,
            "position": mt5.positions_get()[posnum].ticket,
        }
        aaa = mt5.order_send(requestb)
        print(aaa)



    # if position opened is sell
    if mt5.positions_get()[posnum].type == 1 :
        
        while mt5.symbol_info_tick(mt5.positions_get()[posnum].symbol).ask > tpar[numtp+1] :
            time.sleep(0.2)
            continue
        requestb = {
            "action": mt5.TRADE_ACTION_SLTP,
            "symbol": mt5.positions_get()[posnum].symbol,
            "sl": tpar[numtp],
            "tp": mt5.positions_get()[posnum].tp,
            "position": mt5.positions_get()[posnum].ticket,
        }
        aaa = mt5.order_send(requestb)
        print(aaa)

