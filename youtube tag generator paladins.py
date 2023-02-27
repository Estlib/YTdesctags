GT = None
charactertype = None
# while GT != "RC" or GT != "PL" or GT != "RR":
while GT == None:
    GT = input("RC - Rogue Company \nPL - Paladins \nRR - Realm Royale \n Game name: ")
if GT == "RC":
    charactertype = "Rogue"
elif GT == "PL":
    charactertype = "Champion"
elif GT == "RR":
    charactertype = "Class"
CHR = input("Charachter: ")
LVL = input("Map (final fight location for realm): ")
SN = input("Skin: ")
P = input("Current PATCH depicted: ")
IG = ["rogue company","paladins","realm royale"]
SP = " "
SC = ", "
SNW = "skin"
MP = " map"
GP = " gameplay"
internalall = ["rogue","company","realm","royale"]
internalbasic = ["hirez", "roco", "pala"]
GW = ["pro", "tutorial", "tips", "guide", "epic", "new "+charactertype, "tricks"]
Estlibnetwork = ["Estlib", "estlib", "Estlib RoCo", "estlib roco", "Estlib the Space Cat", "Estlib PALA", "estlib paladins", "Estlib RR "]
intgame1= IG[0]+SC+IG[0]+GP+SC+IG[0]+SP+GW[2]+" and "+GW[6]+SC+LVL+SC+IG[0]+SP+CHR+SC+IG[0]+SP+LVL+MP+SC+IG[0]+SP+CHR+SP+SNW+SC+IG[0]+SP+CHR+GP+SC+CHR+SP+IG[0]+SP+SNW+SP+SN+SC+CHR+GP+SC+internalbasic[0]+SC+SNW+SC+MP+SC+GP+SC+internalbasic[1]+SP+GW[1]+SC+GW[0]+SC+GW[2]+SC+GW[3]+SC+GW[6]+SC+P+" patch"+SC+LVL+MP+SC+LVL+" new"+MP+SC+Estlibnetwork[0]+SC+Estlibnetwork[1]+SC+Estlibnetwork[2]+SC+Estlibnetwork[3]+SC+Estlibnetwork[4]+SC
intgame2= IG[1]+SC+IG[1]+GP+SC+IG[1]+SP+GW[2]+" and "+GW[6]+SC+LVL+SC+IG[1]+SP+CHR+SC+IG[1]+SP+LVL+MP+SC+IG[1]+SP+CHR+SP+SNW+SC+IG[1]+SP+CHR+GP+SC+CHR+SP+IG[1]+SP+SNW+SP+SN+SC+CHR+GP+SC+internalbasic[0]+SC+SNW+SC+MP+SC+GP+SC+internalbasic[1]+SP+GW[1]+SC+GW[0]+SC+GW[2]+SC+GW[3]+SC+GW[6]+SC+P+" patch"+SC+LVL+MP+SC+LVL+" new"+MP+SC+Estlibnetwork[0]+SC+Estlibnetwork[1]+SC+Estlibnetwork[5]+SC+Estlibnetwork[6]+SC+Estlibnetwork[4]+SC
intgame3= IG[2]+SC+IG[2]+GP+SC+IG[2]+SP+GW[2]+" and "+GW[6]+SC+LVL+SC+IG[2]+SP+CHR+SC+IG[2]+SP+LVL+MP+SC+IG[2]+SP+CHR+SP+SNW+SC+IG[2]+SP+CHR+GP+SC+CHR+SP+IG[2]+SP+SNW+SP+SN+SC+CHR+GP+SC+internalbasic[0]+SC+SNW+SC+MP+SC+GP+SC+internalbasic[1]+SP+GW[1]+SC+GW[0]+SC+GW[2]+SC+GW[3]+SC+GW[6]+SC+P+" patch"+SC+LVL+MP+SC+LVL+" new"+MP+SC+Estlibnetwork[0]+SC+Estlibnetwork[1]+SC+Estlibnetwork[7]+SC+Estlibnetwork[4]+SC
if GT == "RC":
    print(intgame1)
elif GT == "PL":
    print(intgame2)
elif GT == "RR":
    print(intgame3)


