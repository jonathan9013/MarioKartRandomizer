import random
lightCharacters = ["Toad", "Koopa Troopa", "Shy Guy", "Lakitu", "Toadette", "Baby Mario", "Baby Luigi", "Baby Peach", "Baby Daisy", "Baby Rosalina", "Dry Bones", "Bowser Jr.", "Lemmy", "Larry", "Wendy", "Isabelle"]
mediumCharacters = ["Daisy", "Peach", "Yoshi", "Tanooki Mario", "Cat Peach", "Villager Boy", "Villager Girl", "Inkling Girl", "Inkling Boy", "Mario", "Luigi", "Ludwig", "Iggy"]
heavyCharacters = ["Donkey Kong", "Metal Mario", "Pink Gold Peach", "Rosalina", "Roy", "Waluigi", "Link", "King Boo", "Bowser", "Wario", "Morton", "Dry Bowser"]
characterList = []

karts = ["Standard Kart", "Pipe Frame", "Mach 8", "Steel Driver", "Cat Cruiser", "Circuit Special", "Tri-Speeder", "Badwagon", "Prancer", "Biddybuggy", "Landship", "Sneeker", "Sports Coupe", "Gold Standard", "GLA", "W 25 Silver Arrow", "300 SL Roadster", "Blue Falcon", "Tanooki Kart", "B Dasher", "Streetle", "P-Wing", "Koopa Clown"]
bikes = ["Standard Bike", "The Duke", "Flame Rider", "Varmint", "Mr. Scooty", "Master Cycle Zero", "City Tripper"]
sportsBikes = ["Comet", "Sport Bike", "Jet Bike", "Yoshi Bike", "Master Cycle"]
atvs = ["Standard ATV", "Wild Wiggler", "Teddy Buggy", "Bone Rattler", "Splat Buggy", "Inkstriker"]
kartList = []

tires = ["Standard", "Monster", "Roller", "Slim", "Slick", "Metal", "Button", "Off-Road", "Sponge", "Wood", "Cushion", "Blue Standard", "Hot Monster", "Azure Roller", "Crimson Slim", "Cyber Slick", "Retro Off-Road", "Gold Tires", "GLA Tires", "Triforce Tires", "Ancient Tires", "Leaf Tires"]

gliders = ["Super Glider", "Cloud Glider", "Wario Wing", "Waddle Wing", "Peach Parasol", "Parachute", "Parafoil", "Flower Glider", "Bowser Kite", "Plane Glider", "MKTV Parafoil", "Gold Glider", "Hylian Kite", "Paraglider", "Paper Glider"]

previousSetup = {"character": "",
				 "kart": "",
				 "tire": "",
				 "glider": ""}
currentSetup =  {"character": "",
				 "kart": "",
				 "tire": "",
				 "glider": ""}

tracks = ["Mario Kart Stadium", "Water Park", "Sweet Sweet Canyon", "Thwomp Ruins",
		  "Mario Circuit (Flower Cup)", "Toad Harbor", "Twisted Mansion", "Shy Guy Falls",
		  "Sunshine Airport", "Dolphin Shoals", "Electrodome", "Mount Wario",
		  "Cloudtop Cruise", "Bone-Dry Dunes", "Bowser's Castle", "Rainbow Road (Special Cup)",
		  "Yoshi Circuit", "Excitebike Arena", "Dragon Driftway", "Mute City",
		  "Baby Park", "Cheese Land", "Wild Woods", "Animal Crossing",
		  "Moo Moo Meadows", "Mario Circuit (Shell Cup)", "Cheep Cheep Beach", "Toad's Turnpike",
		  "Dry Dry Desert", "Donut Plains 3", "Royal Raceway", "DK Jungle",
		  "Wario Stadium", "Sherbert Land", "Music Park", "Yoshi Valley",
		  "Tick-Tock Clock", "Piranha Plant Slide", "Grumble Volcano", "Rainbow Road (Lightning Cup)",
		  "Wario's Gold Mine", "Rainbow Road (Triforce Cup)", "Ice Ice Outpost", "Hyrule Circuit",
		  "Neo Bowser City", "Ribbon Road", "Super Bell Subway", "Big Blue",
		  "Paris Promenade", "Toad Circuit", "Choco Mountain", "Coconut Mall",
		  "Tokyo Blur", "Shroom Ridge", "Sky Garden", "Ninja Hideaway",
		  "New York Minute", "Mario Circuit 3", "Kalamari Desert", "Waluigi Pinball",
		  "Sydney Sprint", "Snow Land", "Mushroom Gorge", "Sky-High Sundae"]
usedTracks = []
currentTrack = ""
trackReset = 4

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

def setTrackReset(races):
	global trackReset
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

	if currentSetup["character"] != "":
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
		usedTracks.append(track)
		trackReset = trackReset - 1
		if trackReset == 0:
			usedTracks = []
			trackReset = 4

# def main():
# 	makeLists([],[])
# 	userInput = input("Enter Command: ")
# 	while userInput != 'exit':
# 		match userInput:
# 			case "randomize":
# 				print("Previous setup: ")
# 				print(previousSetup)
# 				print("Current setup: ")
# 				print(currentSetup)
# 				randomize()
# 				print("Previous setup: ")
# 				print(previousSetup)
# 				print("Current setup: ")
# 				print(currentSetup)
# 			case "reroll character":
# 				randomizeAspect("character")
# 				print(currentSetup)
# 			case "reroll kart":
# 				randomizeAspect("kart")
# 				print(currentSetup)
# 			case "reroll tires":
# 				randomizeAspect("tires")
# 				print(currentSetup)
# 			case "reroll glider":
# 				randomizeAspect("glider")
# 				print(currentSetup)
# 			case "randomize track":
# 				randomizeTrack()
# 				print(currentTrack)
# 			case _:
# 				print("Error Unrecognized Command Try Again")
# 		userInput = input("Enter New Command: ")
# 	print("goodbye")

# if __name__=="__main__":
# 	main()