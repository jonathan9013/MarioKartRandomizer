import random
import json
from track import track
from character import character
from cup import cup
from kart import kart
from glider import glider
from tire import tire

lightCharacters = []
mediumCharacters = []
heavyCharacters = []
characterList = []

karts = []
bikes = []
atvs = []
sportsBikes = []
kartList = []

tires = []
gliders = []

previousSetup = {"character": character("", "", ""),
				 "kart": kart("", "", ""),
				 "tire": tire("", ""),
				 "glider": glider("", "")}
currentSetup =  {"character": character("", "", ""),
				 "kart": kart("", "", ""),
				 "tire": tire("", ""),
				 "glider": glider("", "")}

tracks = []
usedTracks = []
currentTrack = track('','','')
trackReset = 4

cups = []
currentCup = cup('','')

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

def randomizeTrack(reroll, reset = 4):
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
			trackReset = reset
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
	global gliders
	global tires
	global karts
	global atvs
	global bikes
	global sportsBikes

	# initialize tracks
	file = open('App\\tracks.json')
	trackData = json.load(file)
	for i in trackData['tracks']:
		tracks.append(track(i['name'], i['cup'], i['image']))
	file.close()

	# initialize characters
	file = open('App\character.json')
	charData = json.load(file)
	for i in charData['characters']:
		if i['weight'] == 'Light':
			lightCharacters.append(character(i['name'], i['weight'], i['image']))
		elif i['weight'] == 'Medium':
			mediumCharacters.append(character(i['name'], i['weight'], i['image']))
		else:
			heavyCharacters.append(character(i['name'], i['weight'], i['image']))
	file.close()

	# initialize cups
	file = open('App\cup.json')
	cupData = json.load(file)
	for i in cupData['cups']:
		cups.append(cup(i['name'], i['image']))
	file.close()

	# initialize karts
	file = open('App\karts.json')
	kartData = json.load(file)
	for i in kartData['karts']:
		if i['style'] == 'Kart':
			karts.append(kart(i['name'], i['image'], i['style']))
		elif i['style'] == 'ATV':
			atvs.append(kart(i['name'], i['image'], i['style']))
		elif i['style'] == 'Bike':
			bikes.append(kart(i['name'], i['image'], i['style']))
		else:
			sportsBikes.append(kart(i['name'], i['image'], i['style']))
	file.close()

	# initialize gliders
	file = open('App\gliders.json')
	gliderData = json.load(file)
	for i in gliderData['gliders']:
		gliders.append(glider(i['name'], i['image']))
	file.close()

	# initialize tires
	file = open('App\\tires.json')
	tireData = json.load(file)
	for i in tireData['tires']:
		tires.append(tire(i['name'], i['image']))
	file.close()
