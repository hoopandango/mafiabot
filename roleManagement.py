import random
import csv

players = []  # List of all players
roles = []  # List of roles in current game
allRolelists = {} # Collection of all rolelists
rolelist = [] # Rolelist used in current game
allRoles = [] # List of all roles [each role is a dictionary]
playercount = 10 # Number of players

def clean():
  global roles
  global rolelist
  global allRoles
  roles.clear()
  rolelist.clear()
  allRoles.clear()
  setAllRoles()
  setAllRolelists()
  setRolelist(playercount)

def tobool(s): 
  return (s=='True')

def setAllRoles():
  with open("RolesData.csv", 'r') as file:
    global allRoles
    reader = csv.DictReader(file)
    for row in reader:
      allRoles.append(row)
    allRoles[-1]["unique"] = tobool(allRoles[-1]["unique"]) 
    
def setAllRolelists():
  global allRolelists
  with open("RolelistData.csv", 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
      allRolelists[row["count"]] = row["roles"].split(";")

def setRolelist(playercount):
  if(playercount >= 8 and playercount <= 16):
    global rolelist 
    rolelist = allRolelists[str(playercount)]

def getRolelist():
  setRolelist(playercount)
  output = "------------Rolelist-------------\n"
  for role in rolelist:
    output += role+"\n"
  output += "\n"
  return output

def setPlayercount(num):  
  global playercount 
  playercount = num

def getPlayers():
  output = "------------Players-------------\n"
  for player in players:
    output += (player+"\n")
  output += "\n"
  return output

def addPlayer(playerlist):
  global players
  playerarray = playerlist.split(',')
  if(len(players)+len(playerarray) <= playercount):
    players += playerarray
  return str(len(playerarray))

def setDefaultPlayers():
  pl = ["Bahamut#6969", "rii#0313","KingdomClasher#9388","ap_G#9765","HiHi1212#7777","weefyeet#5721","Era#4108","Bhand#4260","Cont#2371","Deanx#7687","shaggy#5405","PMC#5844","LordBlu144#1105","Mafira1071#0618","Almighty Poseidon#4897","Pandango#6819" ]
  global players 
  players = pl[0:playercount]

def setRoles(rolelist): #sets roles to roles[]
  rolechoices= []  #roles that can be set in a slot
  global roles
  global allRoles
  #if(playercount <= 11):
  #    allRoles.remove([t for t in allRoles if t["name"] =="Jailor"])
  #    allRoles.remove([t for t in allRoles if t["name"] =="Wolf Apprentice"])
  for e in rolelist:
    if e == "Jailor" or e == "Alphawolf" or e == "Wolf Apprentice":
      rolechoices = [t for t in allRoles if t["name"] == e] 
    elif e == "TI":
      rolechoices = findRolechoices("T","I") 
    elif e == "TP":
      rolechoices = findRolechoices("T","P")   
    elif e == "TK":
      rolechoices = findRolechoices("T","K") 
    elif e == "TS":
      rolechoices = findRolechoices("T","S")   
    else:
      rolechoices = findRolechoices(e[-1]) 
    chosenrole = random.choice(rolechoices) 
    roles.append(chosenrole["name"]) 
    if(chosenrole["unique"]):
      allRoles.remove(chosenrole) 
  return roles

def findRolechoices(faction, *args):
  if(len(args)>0):
    return [t for t in allRoles if t["roletype"] == args[0] and t["faction"] == faction]
  else:
    return [t for t in allRoles if t["faction"] == faction]

def playersStatus():
  output = ""
  if (len(players) == 0):
    output += ("------------Enter " + str(playercount) + " Players------------- \n") 
  elif(len(players) == playercount):
    output += makeRolelist()
  else:
    output += ("need " + str(playercount - len(players)) + " more players \n")
  return output

def makeRolelist():
  global players
  global roles 
  clean()
  roles = setRoles(rolelist)
  random.shuffle(players)
  return printRolelist()

def printRolelist():
  output = ""
  output += ("------------Roles-------------\n") 
  c = 0 
  for entry in rolelist:
    output += (str(c) + " " + entry + " - " + players[c]+ " (" +roles[c]+")\n") 
    c+=1 
  output += "\n"
  return output
