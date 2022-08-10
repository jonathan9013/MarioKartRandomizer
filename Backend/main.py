import random
lightCharacters = ["Toad", "Koopa Troopa", "Shy Guy", "Lakitu", "Toadette", "Baby Mario", "Baby Luigi", "Baby Peach", "Baby Daisy", "Baby Rosalina", "Dry Bones", "Bowser Jr.", "Lemmy", "Larry", "Wendy", "Isabelle"]
mediumCharacters = ["Daisy", "Peach", "Yoshi", "Tanooki Mario", "Cat Peach", "Villager Boy", "Villager Girl", "Inkling Girl", "Inkling Boy", "Mario", "Luigi", "Ludwig", "Iggy"]
heavyCharacters = ["Donkey Kong", "Metal Mario", "Pink Gold Peach", "Rosalina", "Roy", "Waluigi", "Link", "King Boo", "Bowser", "Wario", "Morton", "Dry Bowser"]
characterList = []

karts = ["Standard Kart", "Pipe Frame", "Mach 8", "Steel Driver", "Cat Cruiser", "Circuit Special", "Tri-Speeder", "Badwagon", "Prancer", "Biddybuggy", "LandShip", "Sneeker", "Sports Coupe", "Gold Standard", "GLA", "W 25 Silver Arrow", "300 SL Roadster", "Blue Falcon", "Tanooki Kart", "B Dasher", "Streetle", "P-Wing", "Koopa Clown"]
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
def makeLists(charOpt, kartOpt):
	global characterList
	global kartList
	characterList = []
	kartList= []
	if charOpt == []:
		characterList = lightCharacters+mediumCharacters+heavyCharacters
	else:
		for opt in charOpt:
			if opt == 'light':
				characterList = characterList+lightCharacters
			if opt == 'medium':
				characterList = characterList+mediumCharacters
			if opt == 'heavy':
				characterList = characterList+heavyCharacters
	if kartOpt == []:
		kartList = karts+bikes+sportsBikes+atvs
	else:
		for kart in kartOpt:
			if kart == 'karts':
				kartList = kartList+karts
			if kart == 'bikes':
				kartList = kartList+bikes
			if kart == 'sport bikes':
				kartList = kartList+sportsBikes
			if kart == 'atvs':
				kartList = kartList+atvs
def randomize():
	global previousSetup
	global currentSetup 
	global characterList
	global kartList
	global tires
	global gliders

	character = characterList[random.randint(0, len(characterList)-1)]
	while character == previousSetup["character"]:
		character = characterList[random.randint(0, len(characterList)-1)]
	currentSetup["character"] = character
	previousSetup["character"] = character
	
	kart = kartList[random.randint(0, len(kartList)-1)]
	while kart == previousSetup["kart"]:
		kart = kartList[random.randint(0, len(kartList)-1)]
	currentSetup["kart"] = kart
	previousSetup["kart"] = kart

	tire = tires[random.randint(0, len(tires)-1)]
	while tire == previousSetup["tire"]:
		tire = tires[random.randint(0, len(tires)-1)]
	currentSetup["tire"] = tire
	previousSetup["tire"] = tire

	glider = gliders[random.randint(0, len(gliders)-1)]
	while glider == previousSetup["glider"]:
		glider = gliders[random.randint(0, len(gliders)-1)]
	currentSetup["glider"] = glider
	previousSetup["glider"] = glider

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

def main():
	makeLists([],[])
	userInput = input("Enter Command: ")
	while userInput != 'exit':
		match userInput:
			case "randomize":
				randomize()
				print(currentSetup)
			case "reroll character":
				randomizeAspect("character")
				print(currentSetup)
			case "reroll kart":
				randomizeAspect("kart")
				print(currentSetup)
			case "reroll tires":
				randomizeAspect("tires")
				print(currentSetup)
			case "reroll glider":
				randomizeAspect("glider")
				print(currentSetup)
			case _:
				print("Error Unrecognized Command Try Again")
		userInput = input("Enter New Command: ")
	print("goodbye")

if __name__=="__main__":
	main()