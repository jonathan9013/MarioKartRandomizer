import random
import json
from Track import Track
from Character import Character
from Cup import Cup

lightCharacters = []
mediumCharacters = []
heavyCharacters = []
characterList = []

karts = ["Standard Kart", "Pipe Frame", "Mach 8", "Steel Driver", "Cat Cruiser", "Circuit Special", "Tri-Speeder", "Badwagon", "Prancer", "Biddybuggy", "Landship", "Sneeker", "Sports Coupe", "Gold Standard", "GLA", "W 25 Silver Arrow", "300 SL Roadster", "Blue Falcon", "Tanooki Kart", "B Dasher", "Streetle", "P-Wing", "Koopa Clown"]
bikes = ["Standard Bike", "The Duke", "Flame Rider", "Varmint", "Mr. Scooty", "Master Cycle Zero", "City Tripper"]
sportsBikes = ["Comet", "Sport Bike", "Jet Bike", "Yoshi Bike", "Master Cycle"]
atvs = ["Standard ATV", "Wild Wiggler", "Teddy Buggy", "Bone Rattler", "Splat Buggy", "Inkstriker"]
kartList = []

tires = ["Standard", "Monster", "Roller", "Slim", "Slick", "Metal", "Button", "Off-Road", "Sponge", "Wood", "Cushion", "Blue Standard", "Hot Monster", "Azure Roller", "Crimson Slim", "Cyber Slick", "Retro Off-Road", "Gold Tires", "GLA Tires", "Triforce Tires", "Ancient Tires", "Leaf Tires"]

gliders = ["Super Glider", "Cloud Glider", "Wario Wing", "Waddle Wing", "Peach Parasol", "Parachute", "Parafoil", "Flower Glider", "Bowser Kite", "Plane Glider", "MKTV Parafoil", "Gold Glider", "Hylian Kite", "Paraglider", "Paper Glider"]

previousSetup = {"character": Character("", "", ""),
				 "kart": "",
				 "tire": "",
				 "glider": ""}
currentSetup =  {"character": Character("", "", ""),
				 "kart": "",
				 "tire": "",
				 "glider": ""}

tracks = []
usedTracks = []
currentTrack = Track('','','')
trackReset = 4

cups = []
currentCup = Cup('','')

def getCurrentSetup():
	global currentSetup
	return currentSetup

def getCurrentCharacter():
	global currentSetup
	return currentSetup["character"]

def getCurrentKart():
	global currentSetup
	return currentSetup["kart"]

def getCurrentTire():
	global currentSetup
	return currentSetup["tire"]

def getCurrentGlider():
	global currentSetup
	return currentSetup["glider"]

def getCurrentTrack():
	global currentTrack
	return currentTrack

def getTrackReset():
	global trackReset
	return trackReset

def getCurrentCup():
	return currentCup

def setTrackReset(races):
	global trackReset
	global usedTracks
	usedTracks =[]
	trackReset = races

def makeLists(charOpt, kartOpt):
	global characterList
	global kartList
	characterList = []
	kartList= []
	for opt in charOpt:
		if opt == 'Light':
			characterList = characterList+lightCharacters
		if opt == 'Medium':
			characterList = characterList+mediumCharacters
		if opt == 'Heavy':
			characterList = characterList+heavyCharacters
	for kart in kartOpt:
		if kart == 'Karts':
			kartList = kartList+karts
		if kart == 'Standard Bikes':
			kartList = kartList+bikes
		if kart == 'Sport Bikes':
			kartList = kartList+sportsBikes
		if kart == 'ATVs':
			kartList = kartList+atvs

def randomize():
	global previousSetup
	global currentSetup
	global characterList
	global kartList
	global tires
	global gliders

	if currentSetup["character"].name != "":
		previousSetup = currentSetup.copy()

	character = characterList[random.randint(0, len(characterList)-1)]
	while character == previousSetup["character"]:
		character = characterList[random.randint(0, len(characterList)-1)]
	currentSetup["character"] = character

	kart = kartList[random.randint(0, len(kartList)-1)]
	while kart == previousSetup["kart"]:
		kart = kartList[random.randint(0, len(kartList)-1)]
	currentSetup["kart"] = kart

	tire = tires[random.randint(0, len(tires)-1)]
	while tire == previousSetup["tire"]:
		tire = tires[random.randint(0, len(tires)-1)]
	currentSetup["tire"] = tire

	glider = gliders[random.randint(0, len(gliders)-1)]
	while glider == previousSetup["glider"]:
		glider = gliders[random.randint(0, len(gliders)-1)]
	currentSetup["glider"] = glider

def randomizeAspect(aspect):
	global previousSetup
	global currentSetup
	global characterList
	global kartList
	global tires
	global gliders

	match aspect:
		case "character":
			character = characterList[random.randint(0, len(characterList)-1)]
			while character == previousSetup["character"] and character == currentSetup["character"]:
				character = characterList[random.randint(0, len(characterList)-1)]
			currentSetup["character"] = character
			previousSetup["character"] = character
		case "kart":
			kart = kartList[random.randint(0, len(kartList)-1)]
			while kart == previousSetup["kart"] and kart == currentSetup["kart"]:
				kart = kartList[random.randint(0, len(kartList)-1)]
			currentSetup["kart"] = kart
			previousSetup["kart"] = kart
		case "tires":
			tire = tires[random.randint(0, len(tires)-1)]
			while tire == previousSetup["tire"] and tire == currentSetup["tire"]:
				tire = tires[random.randint(0, len(tires)-1)]
			currentSetup["tire"] = tire
			previousSetup["tire"] = tire
		case "glider":
			glider = gliders[random.randint(0, len(gliders)-1)]
			while glider == previousSetup["glider"] and glider == currentSetup["glider"]:
				glider = gliders[random.randint(0, len(gliders)-1)]
			currentSetup["glider"] = glider
			previousSetup["glider"] = glider

def randomizeTrack(reroll):
	global tracks
	global trackReset
	global usedTracks
	global currentTrack
	track = tracks[random.randint(0, len(tracks)-1)]
	while track in usedTracks:
		track = tracks[random.randint(0, len(tracks)-1)]
	currentTrack = track
	if not reroll:
		trackReset = trackReset - 1
		if trackReset == 0:
			usedTracks = []
			trackReset = 4
	usedTracks.append(track)
		
def randomizeCup():
	global cups
	global currentCup
	cup = cups[random.randint(0, len(cups)-1)]
	while cup == currentCup:
		cup = cups[random.randint(0, len(cups)-1)]
	currentCup = cup

def initialize():
	global tracks
	global lightCharacters
	global mediumCharacters
	global heavyCharacters
	global cups

	file = open('App\\tracks.json')
	trackData = json.load(file)
	for i in trackData['tracks']:
		tracks.append(Track(i['name'], i['cup'], i['image']))
	file.close()
	file = open('App\character.json')
	charData = json.load(file)
	for i in charData['characters']:
		if i['weight'] == 'Light':
			lightCharacters.append(Character(i['name'], i['weight'], i['image']))
		elif i['weight'] == 'Medium':
			mediumCharacters.append(Character(i['name'], i['weight'], i['image']))
		else:
			heavyCharacters.append(Character(i['name'], i['weight'], i['image']))
	file.close()
	file = open('App\cup.json')
	cupData = json.load(file)
	for i in cupData['cups']:
		cups.append(Cup(i['name'], i['image']))
	file.close()

# def main():
# 	initialize()
	# makeLists([],[])
	# userInput = input("Enter Command: ")
	# while userInput != 'exit':
	# 	match userInput:
	# 		case "randomize":
	# 			print("Previous setup: ")
	# 			print(previousSetup)
	# 			print("Current setup: ")
	# 			print(currentSetup)
	# 			randomize()
	# 			print("Previous setup: ")
	# 			print(previousSetup)
	# 			print("Current setup: ")
	# 			print(currentSetup)
	# 		case "reroll character":
	# 			randomizeAspect("character")
	# 			print(currentSetup)
	# 		case "reroll kart":
	# 			randomizeAspect("kart")
	# 			print(currentSetup)
	# 		case "reroll tires":
	# 			randomizeAspect("tires")
	# 			print(currentSetup)
	# 		case "reroll glider":
	# 			randomizeAspect("glider")
	# 			print(currentSetup)
	# 		case "randomize track":
	# 			randomizeTrack()
	# 			print(currentTrack)
	# 		case _:
	# 			print("Error Unrecognized Command Try Again")
	# 	userInput = input("Enter New Command: ")
	# print("goodbye")

# if __name__=="__main__":
# 	main()