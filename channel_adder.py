import keyboard
import gspread
import pyperclip

credentials = {"installed":{"client_id":"884405910879-2kffgh1taeal188dit5pbk7l1165l47q.apps.googleusercontent.com","project_id":"slack-channel-adder","auth_uri":"https://accounts.google.com/o/oauth2/auth","token_uri":"https://oauth2.googleapis.com/token","auth_provider_x509_cert_url":"https://www.googleapis.com/oauth2/v1/certs","client_secret":"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","redirect_uris":["http://localhost"]}}


gc, authorized_user = gspread.oauth_from_dict(credentials)

#sh = gc.open("Channel Adder Master List")
roster = gc.open("Mu Rho Roster Fall 2025")

newlist = roster.get_worksheet(4).batch_get(["C2:C139"]) #gets list of people present at bid day from mu rho roster
rosterPresent = newlist[0]


# newlist = sh.sheet1.batch_get(["D2:D99"])
# presentList = newlist[0]
# #print(presentList)

newlist = roster.get_worksheet(1).batch_get(["L2:L118"]) # gets list of slack names from channel adder master list
slackNameList = newlist[0]

clipboardString = ""

for i in range(len(rosterPresent)):
    if rosterPresent[i][0] == "TRUE":
        clipboardString += slackNameList[i][0]

#print(clipboardString)
pyperclip.copy(clipboardString)
print("READY TO PASTE!")

    