import MetaTrader5 as mt5

mt5.initialize()
cn = 0
for ggg in mt5.positions_get() :
    print(cn)
    cn+=1
    print(ggg)
print()

aa = input("want to close any ? y/n : ")
if aa == "y" :
    i = int(input("which one ? : "))
    ff = mt5.Close(symbol= mt5.positions_get()[i].symbol, ticket= mt5.positions_get()[i].ticket)
    if ff :
        print("done")
