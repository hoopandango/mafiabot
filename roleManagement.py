import random
import csv

players = []
roles = []    #Roles in the game
#rolelist = ["Jailor","TI","TI","TP","TP","TK","TS","RT","RT","RT","Alphawolf","Wolf Apprentice","WW","WW","N","NK"]  #Default Rolelist
allRolelists = []
rolelist = []
allroles = []  #list of all roles
playercount = 15 #default player count

def tobool(s):
  return (s=='True')

def setPlayercount(n):
  playercount = n

def getRolechoices(faction, *args):
  if(len(args)>0):
    return [t for t in allroles if t["roletype"] == args[0] and t["faction"] == faction]
  else:
    return [t for t in allroles if t["faction"] == faction]

def initializeRolelist(playercount):
  with open("RolelistData.csv", 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
      allRolelists[int(row["count"])] = row["roles"].split(";")
    if(playercount >= 8 and playercount <= 16):
      rolelist = allRolelists[playercount]

def initializeAllroles():
  with open("RolesData.csv", 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
      allroles.append(row)
    allroles[-1]["unique"] = tobool(allroles[-1]["unique"]) 

def assignRoles(rolelist): #assigns roles to roles[]
  rolechoices= []  #roles that can be assigned in a slot
  initializeAllroles()
  
  for e in rolelist:
    if e == "Jailor" or e == "Alphawolf" or e == "Wolf Apprentice":
      rolechoices = [t for t in allroles if t["name"] == e] 
    elif e == "TI":
      rolechoices = getRolechoices("T","I") 
    elif e == "TP":
      rolechoices = getRolechoices("T","P")   
    elif e == "TK":
      rolechoices = getRolechoices("T","K") 
    elif e == "TS":
      rolechoices = getRolechoices("T","S")   
    else:
      rolechoices = getRolechoices(e[-1]) 
    chosenrole = random.choice(rolechoices) 
    roles.append(chosenrole["name"]) 
    if(chosenrole["unique"]):
      allroles.remove(chosenrole) 
  return roles

def playersStatus():
  output = ""
  if (len(players) == 0):
    output += ("------------Enter " + str(playercount) + " Players------------- \n") 
  elif(len(players) == playercount):
    output += printRolelist(players)
  else:
    output += ("need " + (len(rolelist) - len(players)) + " more players \n")
  return output

def setDefaultPlayers():
  pl = ["a", "b","c","d","e","f","g","h","i","j","k","l","m","n","o","p" ]
  players = pl[0:playercount]

def addPlayer(player):
  if(len(players) < playercount):
    players.append(player)

def printRolelist(players):
  output = ""
  output += ("------------Roles-------------\n") 
  c = 0 
  initializeRolelist(playercount)
  roles = assignRoles(rolelist)
  random.shuffle(players)
  for entry in rolelist:
    output += (entry + " - " + players[c]+ " (" +roles[c]+")\n") 
    c+=1 
  return output
