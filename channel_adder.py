import keyboard
import gspread
import pyperclip

gc = gspread.oauth()

sh = gc.open("Channel Adder Master List")
roster = gc.open("Mu Rho Roster Fall 2024")

newlist = roster.get_worksheet(3).batch_get(["F2:F99"]) #gets list of people present at bid day from mu rho roster
rosterPresent = newlist[0]


# newlist = sh.sheet1.batch_get(["D2:D99"])
# presentList = newlist[0]
# #print(presentList)

newlist = sh.sheet1.batch_get(["E2:E99"]) # gets list of slack names from channel adder master list
slackNameList = newlist[0]

clipboardString = ""

for i in range(len(rosterPresent)):
    if rosterPresent[i][0] == "TRUE":
        clipboardString += slackNameList[i][0]

#print(clipboardString)
pyperclip.copy(clipboardString)
print("READY TO PASTE!")

    