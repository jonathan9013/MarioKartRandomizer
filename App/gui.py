import PySimpleGUI as gui
from main import *

def get_char_icon(currCharacter):
    match currCharacter:
        case "Baby Daisy":
            return "app\media\characters\MK8_BabyDaisy_Icon.png"
        case "Baby Luigi":
            return "app\media\characters\MK8_BabyLuigi_Icon.png"
        case "Baby Mario":
            return "app\media\characters\MK8_BabyMario_Icon.png"
        case "Baby Peach":
            return "app\media\characters\MK8_BabyPeach_Icon.png"
        case "Baby Rosalina":
            return "app\media\characters\MK8_BabyRosalina_Icon.png"
        case "Bowser":
            return "app\media\characters\MK8_Bowser_Icon.png"
        case "Bowser Jr.":
            return "app\media\characters\MK8_Bowser_Jr_Icon.png"
        case "Cat Peach":
            return "app\media\characters\MK8_Cat_Peach_Icon.png"
        case "Daisy":
            return "app\media\characters\MK8_Daisy_Icon.png"
        case "Donkey Kong":
            return "app\media\characters\MK8_DKong_Icon.png"
        case "Dry Bowser":
            return "app\media\characters\MK8_Dry_Bowser_Icon.png"
        case "Iggy":
            return "app\media\characters\MK8_Iggy_Icon.png"
        case "Isabelle":
            return "app\media\characters\MK8_Isabelle_Icon.png"
        case "Koopa Troopa":
            return "app\media\characters\MK8_Koopa_Icon.png"
        case "Lakitu":
            return "app\media\characters\MK8_Lakitu_Icon.png"
        case "Larry":
            return "app\media\characters\MK8_Larry_Icon.png"
        case "Lemmy":
            return "app\media\characters\MK8_Lemmy_Icon.png"
        case "Link":
            return "app\media\characters\MK8_Link_Icon.png"
        case "Ludwig":
            return "app\media\characters\MK8_Ludwig_Icon.png"
        case "Luigi":
            return "app\media\characters\MK8_Luigi_Icon.png"
        case "Mario":
            return "app\media\characters\MK8_Mario_Icon.png"
        case "Metal Mario":
            return "app\media\characters\MK8_MMario_Icon.png"
        case "Morton":
            return "app\media\characters\MK8_Morton_Icon.png"
        case "Peach":
            return "app\media\characters\MK8_Peach_Icon.png"
        case "Pink Gold Peach":
            return "app\media\characters\MK8_PGPeach_Icon.png"
        case "Rosalina":
            return "app\media\characters\MK8_Rosalina_Icon.png"
        case "Roy":
            return "app\media\characters\MK8_Roy_Icon.png"
        case "Shy Guy":
            return "app\media\characters\MK8_ShyGuy_Icon.png"
        case "Tanooki Mario":
            return "app\media\characters\MK8_Tanooki_Mario_Icon.png"
        case "Toad":
            return "app\media\characters\MK8_Toad_Icon.png"
        case "Toadette":
            return "app\media\characters\MK8_Toadette_Icon.png"
        case "Waluigi":
            return "app\media\characters\MK8_Waluigi_Icon.png"
        case "Wario":
            return "app\media\characters\MK8_Wario_Icon.png"
        case "Wendy":
            return "app\media\characters\MK8_Wendy_Icon.png"
        case "Yoshi":
            return "app\media\characters\MK8_Yoshi_Icon.png"
        case "Dry Bones":
            return "app\media\characters\MK8DX_Dry_Bones_Icon.png"
        case "Inkling Girl":
            return "app\media\characters\MK8DX_Female_Inkling_Icon.png"
        case "King Boo":
            return "app\media\characters\MK8DX_King_Boo_Icon.png"
        case "Inkling Boy":
            return "app\media\characters\MK8DX_Male_Inkling_Icon.png"
        case "Villager Girl":
            return "app\media\characters\VillagerFemale-Icon-MK8.png"
        case "Villager Boy":
            return "app\media\characters\VillagerMale-Icon-MK8.png"

def get_track_icon(currTrack):
	match currTrack:
		case "DK Jungle":
			return "app\media\\tracks\MK8_3DS_DK_Jungle_Course_Icon.png"
		case "Music Park":
			return "app\media\\tracks\MK8_3DS_Music_Park_Course_Icon.png"
		case "Neo Bowser City":
			return "app\media\\tracks\MK8_3DS_Neo_Bowser_City_Course_Icon.png"
		case "Piranha Plant Slide":
			return "app\media\\tracks\MK8_3DS_Piranha_Plant_Slide_Course_Icon.png"
		case "Animal Crossing":
			return "app\media\\tracks\MK8_Animal_Crossing_Course_Icon.png"
		case "Big Blue":
			return "app\media\\tracks\MK8_Big_Blue_Course_Icon.png"
		case "Bone-Dry Dunes":
			return "app\media\\tracks\MK8_Bone-Dry_Dunes_Course_Icon.png"
		case "Bowser's Castle":
			return "app\media\\tracks\MK8_Bowser's_Castle_Course_Icon.png"
		case "Cloudtop Cruise":
			return "app\media\\tracks\MK8_Cloudtop_Cruise_Course_Icon.png"
		case "Dolphin Shoals":
			return "app\media\\tracks\MK8_Dolphin_Shoals_Course_Icon.png"
		case "Dragon Driftway":
			return "app\media\\tracks\MK8_Dragon_Driftway_Course_Icon.png"
		case "Cheep Cheep Beach":
			return "app\media\\tracks\MK8_DS_Cheep_Cheep_Beach_Course_Icon.png"
		case "Tick-Tock Clock":
			return "app\media\\tracks\MK8_DS_Tick-Tock_Clock_Course_Icon.png"
		case "Wario Stadium":
			return "app\media\\tracks\MK8_DS_Wario_Stadium_Course_Icon.png"
		case "Electrodome":
			return "app\media\\tracks\MK8_Electrodrome_Course_Icon.png"
		case "Excitebike Arena":
			return "app\media\\tracks\MK8_Excitebike_Arena_Course_Icon.png"
		case "Cheese Land":
			return "app\media\\tracks\MK8_GBA_Cheese_Land_Course_Icon.png"
		case "Mario Circuit (Shell Cup)":
			return "app\media\\tracks\MK8_GBA_Mario_Circuit_Course_Icon.png"
		case "Ribbon Road":
			return "app\media\\tracks\MK8_GBA_Ribbon_Road_Course_Icon.png"
		case "Baby Park":
			return "app\media\\tracks\MK8_GCN_Baby_Park_Course_Icon.png"
		case "Dry Dry Desert":
			return "app\media\\tracks\MK8_GCN_Dry_Dry_Desert_Course_Icon.png"
		case "Sherbert Land":
			return "app\media\\tracks\MK8_GCN_Sherbet_Land_Course_Icon.png"
		case "Yoshi Circuit":
			return "app\media\\tracks\MK8_GCN_Yoshi_Circuit_Course_Icon.png"
		case "Hyrule Circuit":
			return "app\media\\tracks\MK8_Hyrule_Circuit_Course_Icon.png"
		case "Ice Ice Outpost":
			return "app\media\\tracks\MK8_Ice_Ice_Outpost_Course_Icon.png"
		case "Mario Circuit (Flower Cup)":
			return "app\media\\tracks\MK8_Mario_Circuit_Course_Icon.png"
		case "Mario Kart Stadium":
			return "app\media\\tracks\MK8_Mario_Kart_Stadium_Course_Icon.png"
		case "Mount Wario":
			return "app\media\\tracks\MK8_Mount_Wario_Course_Icon.png"
		case "Mute City":
			return "app\media\\tracks\MK8_Mute_City_Course_Icon.png"
		case "Rainbow Road (Lightning Cup)":
			return "app\media\\tracks\MK8_N64_Rainbow_Road_Course_Icon.png"
		case "Royal Raceway":
			return "app\media\\tracks\MK8_N64_Royal_Raceway_Course_Icon.png"
		case "Toad's Turnpike":
			return "app\media\\tracks\MK8_N64_Toad's_Turnpike_Course_Icon.png"
		case "Yoshi Valley":
			return "app\media\\tracks\MK8_N64_Yoshi_Valley_Course_Icon.png"
		case "Rainbow Road (Special Cup)":
			return "app\media\\tracks\MK8_Rainbow_Road_Course_Icon.png"
		case "Shy Guy Falls":
			return "app\media\\tracks\MK8_Shy_Guy_Falls_Course_Icon.png"
		case "Donut Plains 3":
			return "app\media\\tracks\MK8_SNES_Donut_Plains_3_Course_Icon.png"
		case "Rainbow Road (Triforce Cup)":
			return "app\media\\tracks\MK8_SNES_Rainbow_Road_Course_Icon.png"
		case "Sunshine Airport":
			return "app\media\\tracks\MK8_Sunshine_Airport_Course_Icon.png"
		case "Super Bell Subway":
			return "app\media\\tracks\MK8_Super_Bell_Subway_Course_Icon.png"
		case "Sweet Sweet Canyon":
			return "app\media\\tracks\MK8_Sweet_Sweet_Canyon_Course_Icon.png"
		case "Thwomp Ruins":
			return "app\media\\tracks\MK8_Thwomp_Ruins_Course_Icon.png"
		case "Toad Harbor":
			return "app\media\\tracks\MK8_Toad_Harbor_Course_Icon.png"
		case "Twisted Mansion":
			return "app\media\\tracks\MK8_Twisted_Mansion_Course_Icon.png"
		case "Water Park":
			return "app\media\\tracks\MK8_Water_Park_Course_Icon.png"
		case "Grumble Volcano":
			return "app\media\\tracks\MK8_Wii_Grumble_Volcano_Course_Icon.png"
		case "Moo Moo Meadows":
			return "app\media\\tracks\MK8_Wii_Moo_Moo_Meadows_Course_Icon.png"
		case "Wario's Gold Mine":
			return "app\media\\tracks\MK8_Wii_Wario's_Gold_Mine_Course_Icon.png"
		case "Wild Woods":
			return "app\media\\tracks\MK8_Wild_Woods_Course_Icon.png"
		case "Toad Circuit":
			return "app\media\\tracks\MK8D_3DS_Toad_Circuit_Course_Icon.png"
		case "Shroom Ridge":
			return "app\media\\tracks\MK8D_DS_Shroom_Ridge_Course_Icon.png"
		case "Waluigi Pinball":
			return "app\media\\tracks\MK8D_DS_Waluigi_Pinball_Course_Icon.png"
		case "Sky Garden":
			return "app\media\\tracks\MK8D_GBA_Sky_Garden_Course_Icon.png"
		case "Snow Land":
			return "app\media\\tracks\MK8D_GBA_Snow_Land_Course_Icon.png"
		case "Choco Mountain":
			return "app\media\\tracks\MK8D_N64_Choco_Mountain_Course_Icon.png"
		case "Kalamari Desert":
			return "app\media\\tracks\MK8D_N64_Kalimari_Desert_Course_Icon.png"
		case "Ninja Hideaway":
			return "app\media\\tracks\MK8D_Ninja_Hideaway_Course_Icon.png"
		case "Sky-High Sundae":
			return "app\media\\tracks\MK8D_Sky-High_Sundae_Course_Icon.png"
		case "Mario Circuit 3":
			return "app\media\\tracks\MK8D_SNES_Mario_Circuit_3_Course_Icon.png"
		case "New York Minute":
			return "app\media\\tracks\MK8D_Tour_New_York_Minute_Course_Icon.png"
		case "Paris Promenade":
			return "app\media\\tracks\MK8D_Tour_Paris_Promenade_Course_Icon.png"
		case "Sydney Sprint":
			return "app\media\\tracks\MK8D_Tour_Sydney_Sprint_Course_Icon.png"
		case "Tokyo Blur":
			return "app\media\\tracks\MK8D_Tour_Tokyo_Blur_Course_Icon.png"
		case "Coconut Mall":
			return "app\media\\tracks\MK8D_Wii_Coconut_Mall_Course_Icon.png"
		case "Mushroom Gorge":
			return "app\media\\tracks\MK8D_Wii_Mushroom_Gorge_Course_Icon.png"
		
gui.theme("LightBlue3") # set theme

makeLists([], [])
randomize()
randomizeTrack()
currCharacter = getCurrentCharacter()
currTrack = getCurrentTrack()

char_icon = get_char_icon(currCharacter)
kart_icon = 'app\media\karts\Gold_Standard.png'
tire_icon = 'app\media\\tires\Gold_Tires_MK8.png'
glider_icon = 'app\media\gliders\GoldGliderMK8.png'
track_icon = get_track_icon(currTrack)

layout = [
    [
        gui.Text('Character'),
        gui.Image(filename=char_icon),
        gui.Button('Reroll')
    ],
    [
        gui.Text('Kart'),
        gui.Image(filename=kart_icon),
        gui.Button('Reroll')
    ],
    [
        gui.Text('Tire'),
        gui.Image(filename=tire_icon),
        gui.Button('Reroll')
    ],
    [
        gui.Text('Glider'),
        gui.Image(filename=glider_icon),
        gui.Button('Reroll')
    ],
    [gui.Button('Generate')],
    [
        gui.Checkbox("Karts", default = True, font=('Helvetica', 10)),
        gui.Checkbox("Standard Bikes", default = True, font=('Helvetica', 10)),
        gui.Checkbox("Sport Bikes", default = True, font=('Helvetica', 10)),
        gui.Checkbox("Enable all", default = True, font=('Helvetica', 10, 'bold'))
    ],
    [
        gui.Checkbox("Light", default = True, font=('Helvetica', 10)),
        gui.Checkbox("Medium", default = True, font=('Helvetica', 10)),
        gui.Checkbox("Heavy", default = True, font=('Helvetica', 10)),
        gui.Checkbox("Enable all", default = True, font=('Helvetica', 10, 'bold'))
    ],
    [
        gui.Text('Tracks'),
        gui.Image(filename=track_icon),
        gui.Button('Reroll')
    ],
    [gui.Button('Generate Track')],
]

# Create the Window
window = gui.Window('Mario Kart 8 Deluxe Randomizer', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == gui.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break

    # TODO - add reroll button logic here
    print('End of app')

window.close()
