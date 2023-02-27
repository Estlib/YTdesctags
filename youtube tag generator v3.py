GT = None
charactertype = None
# while GT != "RC" or GT != "PL" or GT != "RR":
DESCmake = input("Generate description? y/n")
DESACstat = "c"
if DESCmake == "y":
    DESCstat = input("Ranked (r), LTM/LTE (l) or casual (c): ")
while GT == None:
    GT = input("RC - Rogue Company \nPL - Paladins \nRR - Realm Royale \nTF2 - Team Fortress 2 \n Game name: ")
if GT == "RC":
    charactertype = "Rogue"
elif GT == "PL":
    charactertype = "Champion"
elif GT == "RR" or GT == "TF2":
    charactertype = "Class"
CHR = input("Charachter: ") #implement tf2 multi character condition: (if more than one like tf2, type tf2)
LVL = input("Map (final fight location for realm): ")
NMAP = input("Is the map most recent one? Empty = no, any = yes: ")
SN = input("Skin, leave empty if no skin or if TF2: ")
P = input("Current PATCH/UPDATE depicted: ")
NP = input("Is the patch/update depicted a new/most recent patch? empty = no, any = yes:")
GM = input("Gamemode: ")
IG = ["rogue company","paladins","realm royale","team fortress 2"]
SP = " "
SC = ","
SNW = "skin"
MP = " map"
GP = " gameplay"
STRand = " and "
PT = " patch"
NW = " new"
NW2 = "new"
internalall = ["rogue","company","realm","royale","team","fortress","classic","2","champions"]
IB = ["hirez", "roco", "pala", "valve"]
GW = ["pro", "tutorial", "tips", "guide", "epic", "new "+charactertype, "tricks"]
Estlibnetwork = ["Estlib", "estlib", "Estlib RoCo", "estlib roco", "Estlib the Space Cat", "Estlib PALA", "estlib paladins", "Estlib RR", "Estlib Realm Royale", "Estlib team fortress 2", "estlib tf2"]
if SN == "" and GT == "RC":
    SN = "base rogue"
elif SN == "" and GT == "PL":
    SN = "stock champ"
elif SN == "" and GT == "RR":
    SN = "default skin"
elif SN == "" and GT == "TF2":
    SN = "no cosmetics"
T01 = [IG[0]+SC,IG[1]+SC,IG[2]+SC,IG[3]+SC]
# example: paladins,
T02 = [IG[0]+GP+SC,IG[1]+GP+SC,IG[2]+GP+SC,IG[3]+GP+SC]
# example: paladins gameplay,
T03 = [IG[0]+SP+GW[2]+STRand+GW[6]+SC,IG[1]+SP+GW[2]+STRand+GW[6]+SC,IG[2]+SP+GW[2]+STRand+GW[6]+SC,IG[3]+SP+GW[2]+STRand+GW[6]+SC]
# example: paladins tips and tricks,
T04map = LVL+SC
# example: frog isle,
T05 = [IG[0]+SP+CHR+SC,IG[1]+SP+CHR+SC,IG[2]+SP+CHR+SC,IG[3]+SP+CHR+SC]
# example: paladins barik,
T06 = [IG[0]+SP+LVL+MP+SC,IG[1]+SP+LVL+MP+SC,IG[2]+SP+LVL+MP+SC,IG[3]+SP+LVL+MP+SC]
# example: paladins frog isle map,
T07 = [IG[0]+SP+CHR+SP+SNW+SC,IG[1]+SP+CHR+SP+SNW+SC,IG[2]+SP+CHR+SP+SNW+SC,IG[3]+SP+CHR+SP+SNW+SC]
# example: paladins barik skin, 
T08 = [IG[0]+SP+CHR+GP+SC,IG[1]+SP+CHR+GP+SC,IG[2]+SP+CHR+GP+SC,IG[3]+SP+CHR+GP+SC]
# example: paladins barik gameplay,
T09 = [CHR+SP+IG[0]+SP+SNW+SP+SN+SC,CHR+SP+IG[1]+SP+SNW+SP+SN+SC,CHR+SP+IG[2]+SP+SNW+SP+SN+SC,CHR+SP+IG[3]+SP+SNW+SP+SN+SC]
# example: barik paladins skin steel forged,
T10cgp = CHR+GP+SC
# example: barik gameplay,
T11skn = SNW+SC
# example: steel forged,
T12mgp = MP+SP+GP+SC
# example: frog isle gameplay,
T13 = [IB[1]+SP+GW[1]+SC,IB[2]+SP+GW[1]+SC,internalall[2]+SP+internalall[3]+SP+GW[1]+SC,internalall[4]+SP+internalall[5]+SP+internalall[6]+SP+GW[1]+SC]
# example: roco tutorial,
T14 = GW[0]+GP+SC
# example: pro gameplay,
T15 = P+PT+SC
# example: nightfall patch,
T16 = [IG[0]+SP+P+PT+SC,IG[1]+SP+P+PT+SC,IG[2]+SP+P+PT+SC,IG[3]+SP+P+PT+SC]
# example: paladins nightfall patch,
T17 = LVL+MP+SC
# example: frog isle map, T[]
T18 = [IG[0]+SP+LVL+NW+MP+SC,IG[1]+SP+LVL+NW+MP+SC,IG[2]+SP+LVL+NW+MP+SC,IG[3]+SP+LVL+NW+MP+SC]
# example: paladins frog isle new map, ADDED ONLY IF MAP IS NEW
T19 = [IG[0]+SP+LVL+MP+SC,IG[1]+SP+LVL+MP+SC,IG[2]+SP+LVL+MP+SC,IG[3]+SP+LVL+MP+SC]
# example: paladins frog isle map, ADDED ONLY IF MAP IS OLD
T20 = [Estlibnetwork[0]+Estlibnetwork[1]+Estlibnetwork[4]+Estlibnetwork[2]+Estlibnetwork[3],Estlibnetwork[0]+Estlibnetwork[1]+Estlibnetwork[4]+Estlibnetwork[5]+Estlibnetwork[6],Estlibnetwork[0]+Estlibnetwork[1]+Estlibnetwork[4]+Estlibnetwork[7]+Estlibnetwork[8],Estlibnetwork[0]+Estlibnetwork[1]+Estlibnetwork[4]+Estlibnetwork[9]+Estlibnetwork[10],]
# example: Estlib,estlib,Estlib RoCo,estlib roco,Estlib the Space Cat,Estlib PALA,estlib paladins,Estlib RR,Estlib Realm Royale,Estlib team fortress 2,estlib tf2
T21 = [NW2+PT+SP+P+SC+NW2+SP+IG[0]+PT+SP+P,NW2+PT+SP+P+SC+NW2+SP+IG[1]+PT+SP+P,NW2+PT+SP+P+SC+NW2+SP+IG[2]+PT+SP+P,NW2+PT+SP+P+SC+NW2+SP+IG[3]+PT+SP+P]
# example: new 
COND1 = ["no condition <<<","no condition <<<","no condition <<<","no condition <<<"]
if NMAP != "":
    COND1[0] = T18[0]
    COND1[1] = T18[1]
    COND1[2] = T18[2]
    COND1[3] = T18[3]
else:
    COND1[0] = T19[0]
    COND1[1] = T19[1]
    COND1[2] = T19[2]
    COND1[3] = T19[3]
COND2 = ["no condition 2 <<<","no condition 2 <<<","no condition 2 <<<","no condition 2 <<<"]
if NP != "":
    COND2[0] = T21[0]
    COND2[1] = T21[1]
    COND2[2] = T21[2]
    COND2[3] = T21[3]
else:
    COND2[0] = ""
    COND2[1] = ""
    COND2[2] = ""
    COND2[3] = ""
roguestring= T01[0]+T02[0]+T03[0]+T04map+T05[0]+T06[0]+T07[0]+T08[0]+T09[0]+T10cgp+IB[0]+SC+T11skn+T12mgp+T13[0]+T14+T15+T16[0]+T17+COND1[0]+COND2[0] #+++++++++++++
realmstring= T01[2]+T02[2]+T03[2]+T04map+T05[2]+T06[2]+T07[2]+T08[2]+T09[2]+T10cgp+IB[0]+SC+T11skn+T12mgp+T13[2]+T14+T15+T16[2]+T17+COND1[2]+COND2[2] #+++++++++++++
palastring= T01[1]+T02[1]+T03[1]+T04map+T05[1]+T06[1]+T07[1]+T08[1]+T09[1]+T10cgp+IB[0]+SC+T11skn+T12mgp+T13[1]+T14+T15+T16[1]+T17+COND1[1]+COND2[1] #+++++++++++++
tf2stringH= T01[3]+T02[3]+T03[3]+T04map+T05[3]+T06[3]+T07[3]+T08[3]+T09[3]+T10cgp+IB[3]+SC+T11skn+T12mgp+T13[3]+T14+T15+T16[3]+T17+COND1[3]+COND2[3] #+++++++++++++
def descriptiongenerator():
    print("==================================")
    if GT == "RC" and DESCstat == "c": #rogue company casual
        print(IG[0]+" match info:")
        print("")
        print(" - Rogue: "+CHR.capitalize())
        print(" - Map: "+LVL.capitalize())
        print(" - Patch: "+P.capitalize())
        print(" - Gamemode: "+GM.capitalize())
        print(" - Skin: "+SN.capitalize())
        print(" - Scoreboard rank: "+RSCORE)
        print("==================================")
        print("Main Youtube Channel - https://www.youtube.com/estlib")
    elif GT == "RC" and DESCstat == "r": #rogue company ranked
        print("")
        print("Error, no ranked description layout yet.")
        print("")
        print(IG[0]+" match info:")
        print("")
        print(" - Rogue: "+CHR.capitalize())
        print(" - Map: "+LVL.capitalize())
        print(" - Patch: "+P.capitalize())
        print(" - Gamemode: "+GM.capitalize())
        print(" - Skin: "+SN.capitalize())
        print(" - Scoreboard rank: "+RSCORE)
        print("==================================")
        print("Main Youtube Channel - https://www.youtube.com/estlib")
    elif GT == "RC" and DESCstat == "l": #rogue company ltm/lte
        print("")
        print("Error, no LTM/LTE description layout yet.")
        print("")
        print(IG[0]+" match info:")
        print("")
        print(" - Rogue: "+CHR.capitalize())
        print(" - Map: "+LVL.capitalize())
        print(" - Patch: "+P.capitalize())
        print(" - Gamemode: "+GM.capitalize())
        print(" - Skin: "+SN.capitalize())
        print(" - Scoreboard rank: "+RSCORE)
        print("==================================")
        print("Main Youtube Channel - https://www.youtube.com/estlib")
    elif GT == "PL" and DESCstat == "c": #paladins casual
        print(IG[1]+" match info:")
        print("")
        print(" - Champion: "+CHR.capitalize())
        print(" - Map: "+LVL.capitalize())
        print(" - Patch: "+P.capitalize())
        print(" - Gamemode: "+GM.capitalize())
        print(" - Class Objective: "+CO)
        print(" - Skin: "+SN.capitalize())
        print(" - Accolades: "+Paccol)
        print("==================================")
        print("Main Channel - https://www.youtube.com/estlib")
        print("Rogue Company Channel - https://www.youtube.com/channel/UC2wfziK4S0nSp3-AV2p0XXg")
    elif GT == "PL" and DESCstat == "r": #paladins ranked
        print(IG[1]+" ranked match info:")
        print("")
        print(" - Pick ladder position: "+rankpickladder)
        print(" - Champion: "+CHR.capitalize())
        print(" - Map: "+LVL.capitalize())
        print(" - Season/Split: "+rankseasonsplit)
        print(" - Class Objective: "+CO)
        print(" - Result: "+rankresult)
        if isTPavailable == "":
            print(" - Amount: Not available for this match.")
        else:
            TPcalc = int(currentTP)-int(addTP)
            print(" - Amount: "+currentrank+"["+str(TPcalc)+"]TP + ["+str(addTP)+"]TP")
        print(" - Skin: "+SN.capitalize())
        print(" - Credits (Team/Overall rank): "+rankteamcredit)
        print(" - Match ID: "+matchid)  
        print("==================================")
        print("Main Channel - https://www.youtube.com/estlib")
        print("Rogue Company Channel - https://www.youtube.com/channel/UC2wfziK4S0nSp3-AV2p0XXg")
    elif GT == "PL" and DESCstat == "l": #paladins ltm
        print(IG[1]+" match info:")
        print("")
        print(" - Mode Name: "+ltmname.capitalize())
        print(" - Mode Edition: "+ltmrelease.capitalize())
        print(" - Mode Description: "+ltmdescription.capitalize())
        print(" - Map: "+LVL.capitalize())
        print(" - Gamemode: "+ltmgamemode.capitalize())
        print(" - Date of LTM: "+ltmdate)
        print(" - Skin: "+SN.capitalize())
        print("==================================")
        print("Main Channel - https://www.youtube.com/estlib")
        print("Rogue Company Channel - https://www.youtube.com/channel/UC2wfziK4S0nSp3-AV2p0XXg")
    elif GT == "RR" and DESCstat == "c": #realm casual
        print(IG[2]+" match info:")
        print("")
        print(" - Class: "+CHR.capitalize())
        print(" - Subclass: "+LVL.capitalize())
        print(" - Patch: "+P.capitalize())
        print(" - Queue type: "+QT.capitalize())
        print(" - Queue configuration: "+QC)
        print(" - Position: "+RSCORE)
        print(" - Skin: "+SN.capitalize())
        print(" - Kills: "+Kcount)
        print("==================================")
        print("Main Youtube Channel - https://www.youtube.com/estlib")
    elif GT == "RR" and DESCstat == "r": #realm ranked
        print("")
        print("Error, no ranked description layout yet.")
        print("")
        print(IG[2]+" match info:")
        print("")
        print(" - Class: "+CHR.capitalize())
        print(" - Subclass: "+LVL.capitalize())
        print(" - Patch: "+P.capitalize())
        print(" - Queue type: "+QT.capitalize())
        print(" - Queue configuration: "+QC)
        print(" - Position: "+RSCORE)
        print(" - Skin: "+SN.capitalize())
        print(" - Kills: "+Kcount)
        print("==================================")
        print("Main Youtube Channel - https://www.youtube.com/estlib")
    elif GT == "TF2" and DESCstat == "c": #tf2 casual
        print("Main Channel - https://www.youtube.com/estlib")
        print("Rogue Company Channel - https://www.youtube.com/channel/UC2wfziK4S0nSp3-AV2p0XXg")
    elif GT == "TF2" and DESCstat == "r": #tf2 ranked
        print("")
        print("Error, no ranked description layout yet.")
        print("")
        print("Main Channel - https://www.youtube.com/estlib")
        print("Rogue Company Channel - https://www.youtube.com/channel/UC2wfziK4S0nSp3-AV2p0XXg")
    print("Bitchute - https://www.bitchute.com/channel/ysZEbPDc5fMQ/")
    print("Twitch - https://www.twitch.tv/estlibyt")
    print("Twitter - https://twitter.com/estlib")
    print("Discord server - https://discord.gg/tWU6S2r")
    print("Soundcloud - https://soundcloud.com/estlib/")
    print("Bandcamp - https://estlib.bandcamp.com/")
    print("Battle of the Bits - https://battleofthebits.org/barracks/Profile/Estlib/")
    print("Steam Workshop - https://steamcommunity.com/id/estlib/myworkshopfiles/?appid=440")
    print("==================================")
RCSCORE = "none"
CO = "none"
Paccol = "No"
SubC = "None"
QT = "unknown/LTM"
Tcount = "1"
QC = "none"
Kcount = "0"
rankpickladder = "0"
rankseasonsplit = "4/1"
rankresult = "Win"
currentrank = "Plat"
currentTP = 0
addTP = 0
addrank = "none"
rankteamcredit = "0/0"
matchid = "0"

ltmname = "0"
ltmrelease = "1st Release"
ltmdescription = "0"
ltmdate = "0"
ltmgamemode = "0"

if DESCmake == "y":
    if GT == "RC" and DESCstat == "c":
        RSCORE = input("Scoreboard rank rogue company (1st, 2nd etc): ")
    elif GT == "PL" and DESCstat == "c":
        CO = input("Class objective paladins (Yes or No/amount): ")
        Paccol = input("Accolades paladins (ex: Skill x1 / Teamwork x2, if none, leave empty): ")
        if Paccol == "":
            Paccol = "No"
    elif GT == "RR" and DESCstat == "c":
        SubC = input("Subclass realm royale (Axe, Arbalest etc, if none, leave empty): ")
        QT = input("Queue type (Solo - 1, Duo - 2, Squad - 3")
        if QT == "1":
            QT = "Solo"
        elif QT == "2":
            QT = "Duo"
        elif QT == "3":
            QT = "Squad"
        Tcount = input("how many players in your team including you?: ")
        if Tcount == "1":
            if QT =="Solo":
                QC = "1 v 1"
            elif QT =="Duo":
                QC = "1 v 2"
            elif QT =="Squad":
                QC = "1 v 4"
        elif Tcount == "2":
            if QT =="Solo":
                QC = "2 v 1"
            elif QT =="Duo":
                QC = "2 v 2"
            elif QT =="Squad":
                QC = "2 v 4"
        elif Tcount == "3":
            if QT =="Solo":
                QC = "3 v 1"
            elif QT =="Duo":
                QC = "3 v 2"
            elif QT =="Squad":
                QC = "3 v 4"
        elif Tcount == "4":
            if QT =="Solo":
                QC = "4 v 1"
            elif QT =="Duo":
                QC = "4 v 2"
            elif QT =="Squad":
                QC = "4 v 4"
        RSCORE = input("Final position realm (1st, 2nd etc): ")
        Kcount = input("Kills(/teamkills) teamkills only if in a team: ")
    elif GT == "RC" and DESCstat == "r":
        RSCORE = input("Scoreboard rank rogue company (1st, 2nd etc): ")        
    elif GT == "PL" and DESCstat == "r":
        CO = input("Class objective paladins (Yes or No/amount): ")
        rankpickladder = input("Pick ladder position: ")
        print("season/split is set to "+rankseasonsplit+", not asking. Change in predef file.")
        print("match result is set to "+rankresult+", not asking. Change in predef file.")
        currentrank = input("B-ronze, S-ilver, G-old, P-latinum, M-asters, g-R-andmasters")
        if currentrank == "B":
            currentrank == "Bronze"
        elif currentrank == "S":
            currentrank == "Silver"
        elif currentrank == "G":
            currentrank == "Gold"
        elif currentrank == "P":
            currentrank == "Platinum"
        elif currentrank == "M":
            currentrank == "Masters"
        elif currentrank == "R":
            currentrank == "Grandmasters"
        isTPavailable = input("is the rank TP screen visible? enter = no, any = yes")
        currentTP = input("TP total after match")
        addTP = input("TP gained in match")
        print("cannot add rank up to data. current is: "+addrank+", not asking.")
        rankteamcredit = input("team rank in credits / overall rank in credits. ex: 3/5")
        matchid = input("type match id, enter to skip if not available:")
        if matchid == "":
            matchid = "Not available for this match"
    elif GT == "RR" and DESCstat == "r":
        SubC = input("Subclass realm royale (Axe, Arbalest etc, if none, leave empty): ")
        QT = input("Queue type (Solo - 1, Duo - 2, Squad - 3")
        if QT == "1":
            QT = "Solo"
        elif QT == "2":
            QT = "Duo"
        elif QT == "3":
            QT = "Squad"
        Tcount = input("how many players in your team including you?: ")
        if Tcount == "1":
            if QT =="Solo":
                QC = "1 v 1"
            elif QT =="Duo":
                QC = "1 v 2"
            elif QT =="Squad":
                QC = "1 v 4"
        elif Tcount == "2":
            if QT =="Solo":
                QC = "2 v 1"
            elif QT =="Duo":
                QC = "2 v 2"
            elif QT =="Squad":
                QC = "2 v 4"
        elif Tcount == "3":
            if QT =="Solo":
                QC = "3 v 1"
            elif QT =="Duo":
                QC = "3 v 2"
            elif QT =="Squad":
                QC = "3 v 4"
        elif Tcount == "4":
            if QT =="Solo":
                QC = "4 v 1"
            elif QT =="Duo":
                QC = "4 v 2"
            elif QT =="Squad":
                QC = "4 v 4"
        RSCORE = input("Final position realm (1st, 2nd etc): ")
        Kcount = input("Kills(/teamkills) teamkills only if in a team: ")
    elif GT == "RC" and DESCstat == "l":
        RSCORE = input("Scoreboard rank rogue company (1st, 2nd etc): ")
    elif GT == "PL" and DESCstat == "l":
        ltmname = input("Name of ltm: ")
        ltmrelease = input("if ltm has first appeared - 1, else r: ")
        if ltmrelease == "1":
            ltmrelease = "1st Release"
        elif ltmrelease == "r":
            ltmrelease = "Returning mode"
        ltmdescription = input("Description of the ltm: ")
        ltmdate = input("date of ltm: ")
        ltmgamemode = input("gamemode of ltm, can be multiple: ")
    elif GT == "RR" and DESCstat == "l":
        SubC = input("Subclass realm royale (Axe, Arbalest etc, if none, leave empty): ")
        QT = input("Queue type (Solo - 1, Duo - 2, Squad - 3")
        if QT == "1":
            QT = "Solo"
        elif QT == "2":
            QT = "Duo"
        elif QT == "3":
            QT = "Squad"
        Tcount = input("how many players in your team including you?: ")
        if Tcount == "1":
            if QT =="Solo":
                QC = "1 v 1"
            elif QT =="Duo":
                QC = "1 v 2"
            elif QT =="Squad":
                QC = "1 v 4"
        elif Tcount == "2":
            if QT =="Solo":
                QC = "2 v 1"
            elif QT =="Duo":
                QC = "2 v 2"
            elif QT =="Squad":
                QC = "2 v 4"
        elif Tcount == "3":
            if QT =="Solo":
                QC = "3 v 1"
            elif QT =="Duo":
                QC = "3 v 2"
            elif QT =="Squad":
                QC = "3 v 4"
        elif Tcount == "4":
            if QT =="Solo":
                QC = "4 v 1"
            elif QT =="Duo":
                QC = "4 v 2"
            elif QT =="Squad":
                QC = "4 v 4"
        RSCORE = input("Final position realm (1st, 2nd etc): ")
        Kcount = input("Kills(/teamkills) teamkills only if in a team: ")
    descriptiongenerator()
    
if GT == "RC"and DESCstat == "c":
    print(roguestring)
elif GT == "PL"and DESCstat == "c":
    print(palastring)
elif GT == "RR"and DESCstat == "c":
    print(realmstring)
elif GT == "TF2"and DESCstat == "c":
    print(tf2stringH)
elif GT == "RC"and DESCstat == "l":
    print(roguestring)
elif GT == "PL"and DESCstat == "l":
    print(palastring)
elif GT == "RR"and DESCstat == "l":
    print(realmstring)
elif GT == "TF2"and DESCstat == "l":
    print(tf2stringH)
elif GT == "RC"and DESCstat == "r":
    print(roguestring)
elif GT == "PL"and DESCstat == "r":
    print(palastring)
elif GT == "RR"and DESCstat == "r":
    print(realmstring)
elif GT == "TF2"and DESCstat == "r":
    print(tf2stringH)
# scraps:
#
# T01gameRC = IG[0]+SC
# T01gamePL = IG[1]+SC
# T01gameRR = IG[2]+SC
# T01gameTF2 = IG[3]+SC
# T02gpRC = IG[0]+GP+SC
# T02gpPL = IG[1]+GP+SC
# T02gpRR = IG[2]+GP+SC
# T02gpTF2 = IG[3]+GP+SC
# T03gamettRC = IG[0]+SP+GW[2]+STRand+GW[6]+SC
# T03gamettPL = IG[1]+SP+GW[2]+STRand+GW[6]+SC
# T03gamettRR = IG[2]+SP+GW[2]+STRand+GW[6]+SC
# T03gamettTF2 = IG[3]+SP+GW[2]+STRand+GW[6]+SC
# T05gamecharRC = IG[0]+SP+CHR+SC
# T05gamecharPL = IG[1]+SP+CHR+SC
# T05gamecharRR = IG[2]+SP+CHR+SC
# T05gamecharTF2 = IG[3]+SP+CHR+SC
# T06gamemapRC = IG[0]+SP+LVL+MP+SC
# T06gamemapPL = IG[1]+SP+LVL+MP+SC
# T06gamemapRR = IG[2]+SP+LVL+MP+SC
# T06gamemapTF2 = IG[3]+SP+LVL+MP+SC
# T07charskinRC = IG[0]+SP+CHR+SP+SNW+SC
# T07charskinPL = IG[1]+SP+CHR+SP+SNW+SC
# T07charskinRR = IG[2]+SP+CHR+SP+SNW+SC
# T07charskinTF2 = IG[3]+SP+CHR+SP+SNW+SC
# T08gamechargpRC = IG[0]+SP+CHR+GP+SC
# T08gamechargpPL = IG[1]+SP+CHR+GP+SC
# T08gamechargpRR = IG[2]+SP+CHR+GP+SC
# T08gamechargpTF2 = IG[3]+SP+CHR+GP+SC