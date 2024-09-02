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

tpar = [pos.price_open]

for i in range(tpcount):
    tpar.append(float(input(f" tp{i+1} : ")))

print(tpar)

for numtp in range(tpcount):
    # if position opened is buy
    if pos.type == 0 :
        
        while mt5.symbol_info_tick(mt5.positions_get()[posnum].symbol).bid < tpar[numtp+1] :
            continue
        requestb = {
            "action": mt5.TRADE_ACTION_SLTP,
            "symbol": pos.symbol,
            "sl": tpar[numtp],
            "tp": pos.tp,
            "position": pos.ticket,
        }
        aaa = mt5.order_send(requestb)
        print(aaa)



    # if position opened is sell
    if pos.type == 1 :
        
        while mt5.symbol_info_tick(mt5.positions_get()[posnum].symbol).ask > tpar[numtp+1] :
            continue
        requestb = {
            "action": mt5.TRADE_ACTION_SLTP,
            "symbol": pos.symbol,
            "sl": tpar[numtp],
            "tp": pos.tp,
            "position": pos.ticket,
        }
        aaa = mt5.order_send(requestb)
        print(aaa)

        
