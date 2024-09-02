# this python script used to read your MT5 that is opened on your device and show your opened positions on your terminals 
# then it let you choose one of them to close it instantly
# this script isnt designed to be used alone, it will not make any sense, its mainly made to be used in some other bigger projects like gui applications
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
