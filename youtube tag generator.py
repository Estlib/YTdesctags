GT = input("RC - Rogue Company \nPL - Paladins \nRR - Realm Royale \n Game name: ")
CHR = input("Charachter: ")
LVL = input("Map (final fight location for realm): ")
SN = input("Skin: ")
P = input("Current PATCH depicted: ")
charactertype = None
if GT == "RC":
    charactertype = "Rogue"
elif GT == "PL":
    charactertype = "Champion"
elif GT == "RR":
    charactertype = "Class"
IG = ["rogue company","paladins","realm royale"]
SP = " "
SC = ", "
SNW = "skin"
MP = " map"
GP = " gameplay"
internalall = ["rogue","company","realm","royale"]
internalbasic = ["hirez", "roco", "pala"]
GW = ["pro", "tutorial", "tips", "guide", "epic", "new "+charactertype, "tricks"]
Estlibnetwork = ["Estlib", "estlib", "Estlib RoCo", "estlib roco", "Estlib the Space Cat"]
intgame1= IG[0]+SC+IG[0]+GP+SC+IG[0]+SP+GW[2]+" and "+GW[6]+SC+LVL+SC+IG[0]+SP+CHR+SC+IG[0]+SP+LVL+MP+SC+IG[0]+SP+CHR+SP+SNW+SC+IG[0]+SP+CHR+GP+SC+CHR+SP+IG[0]+SP+SNW+SP+SN+SC+CHR+GP+SC+internalbasic[0]+SC+SNW+SC+MP+SC+GP+SC+internalbasic[1]+SP+GW[1]+SC+GW[0]+SC+GW[2]+SC+GW[3]+SC+GW[6]+SC+P+" patch"+SC+LVL+MP+SC+LVL+" new"+MP+SC+Estlibnetwork[0]+SC+Estlibnetwork[1]+SC+Estlibnetwork[2]+SC+Estlibnetwork[3]+SC+Estlibnetwork[4]+SC
if GT == "RC":
    print(intgame1)
elif GT == "PL":
    print(intgame1)
elif GT == "RR":
    print(intgame1)


