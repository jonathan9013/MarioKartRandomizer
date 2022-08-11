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

def get_kart_icon(currKart):
    match currKart:
        # atvs
        case "Bone Rattler":
            return "app\media\\atvs\MK8BoneRattler.png"
        case "Inkstriker":
            return "app\media\\atvs\MK8DX_Inkstriker.png"
        case "Splat Buggy":
            return "app\media\\atvs\MK8DX_Splat_Buggy.png"
        case "Standard ATV":
            return "app\media\\atvs\StandardATVBodyMK8.png"
        case "Teddy Buggy":
            return "app\media\\atvs\TeddyBuggyBodyMK8.png"
        case "Wild Wiggler":
            return "app\media\\atvs\WildWigglerBodyMK8.png"
        # standard bikes
        case "Flame Rider":
            return "app\media\\bikes\FlameRiderBodyMK8.png"
        case "City Tripper":
            return "app\media\\bikes\MK8_Light-Green_City_Tripper.png"
        case "Master Cycle Zero":
            return "app\media\\bikes\MK8D_Master_Cycle_Zero.png"
        case "Mr. Scooty":
            return "app\media\\bikes\MrScootyBodyMK8.png"
        case "Standard Bike":
            return "app\media\\bikes\StandardBikeBodyMK8.png"
        case "The Duke":
            return "app\media\\bikes\TheDukeBodyMK8.png"
        case "Varmint":
            return "app\media\\bikes\VarmintBodyMK8.png"
        # sport bikes
        case "Comet":
            return "app\media\sport_bikes\CometBodyMK8.png"
        case "Jet Bike":
            return "app\media\sport_bikes\JetBikeBodyMK8.png"
        case "Master Cycle":
            return "app\media\sport_bikes\MK8MasterCycle.png"
        case "Sport Bike":
            return "app\media\sport_bikes\SportBikeBodyMK8.png"
        case "Yoshi Bike":
            return "app\media\sport_bikes\YoshiBikeBodyMK8.png"
        # karts
        case "300 SL Roadster":
            return "app\media\karts\\300SLRoadster_MK8.png"
        case "Badwagon":
            return "app\media\karts\BadwagonBodyMK8.png"
        case "Biddybuggy":
            return "app\media\karts\BiddybuggyBodyMK8.png"
        case "Cat Cruiser":
            return "app\media\karts\CatCruiserBodyMK8.png"
        case "Circuit Special":
            return "app\media\karts\CircuitSpecialBodyMK8.png"
        case "GLA":
            return "app\media\karts\GLA-MK8.png"
        case "Gold Standard":
            return "app\media\karts\Gold_Standard.png"
        case "Landship":
            return "app\media\karts\LandshipBodyMK8.png"
        case "Mach 8":
            return "app\media\karts\Mach8BodyMK8.png"
        case "Tanooki Kart":
            return "app\media\karts\MK8_Tanooki_Buggy_Sprite.png"
        case "Blue Falcon":
            return "app\media\karts\MK8BlueFalcon.png"
        case "Koopa Clown":
            return "app\media\karts\MK8DX_Koopa_Clown.png"
        case "P-Wing":
            return "app\media\karts\MK8PWing.png"
        case "Streetle":
            return "app\media\karts\MK8Streetle.png"
        case "Pipe Frame":
            return "app\media\karts\PipeFrameBodyMK8.png"
        case "Prancer":
            return "app\media\karts\PrancerBodyMK8.png"
        case "Sneeker":
            return "app\media\karts\SneakerBodyMK8.png"
        case "Sports Coupe":
            return "app\media\karts\SportsCoupeMK8.png"
        case "Standard Kart":
            return "app\media\karts\StandardKartBodyMK8.png"
        case "Steel Driver":
            return "app\media\karts\Steel_Driver.png"
        case "Tri-Speeder":
            return "app\media\karts\TrispeederBodyMK8.png"
        case "W 25 Silver Arrow":
            return "app\media\karts\W25SilverArrow-MK8.png"
        case "B Dasher":
            return "app\media\karts\ZeldaMK8Bdasher.png"

def get_tire_icon(currTire):
    match currTire:
        case "Azure Roller":
            return "app\media\\tires\AzureRollerTiresMK8.png"
        case "Blue Standard":
            return "app\media\\tires\Blue_Standard.png"
        case "Button":
            return "app\media\\tires\ButtonTiresMK8.png"
        case "Crimson Slim":
            return "app\media\\tires\CrimsonSlimTiresMK8.png"
        case "Cushion":
            return "app\media\\tires\CushionTiresMK8.png"
        case "Cyber Slick":
            return "app\media\\tires\CyberSlickTiresMK8.png"
        case "GLA Tires":
            return "app\media\\tires\GLATires-MK8.png"
        case "Gold Tires":
            return "app\media\\tires\Gold_Tires_MK8.png"
        case "Hot Monster":
            return "app\media\\tires\HotMonsterTiresMK8.png"
        case "Leaf Tires":
            return "app\media\\tires\Leaf_Tires_MK8.png"
        case "Metal":
            return "app\media\\tires\MetalTiresMK8.png"
        case "Triforce Tires":
            return "app\media\\tires\MK8-TriforceTires.png"
        case "Ancient Tires":
            return "app\media\\tires\MK8D_Ancient_Tires.png"
        case "Monster":
            return "app\media\\tires\MonsterTiresMK8.png"
        case "Off-Road":
            return "app\media\\tires\Off-Road.png"
        case "Retro Off-Road":
            return "app\media\\tires\Retro_Off-Road.png"
        case "Roller":
            return "app\media\\tires\RollerTiresMK8.png"
        case "Slick":
            return "app\media\\tires\SlickTiresMK8.png"
        case "Slim":
            return "app\media\\tires\SlimTiresMK8.png"
        case "Sponge":
            return "app\media\\tires\SpongeTiresMK8.png"
        case "Standard":
            return "app\media\\tires\StandardTiresMK8.png"
        case "Wood":
            return "app\media\\tires\WoodTiresMK8.png"

def get_glider_icon(currGlider):
    match currGlider:
        case "Bowser Kite":
            return "app\media\gliders\BowserKiteMK8.png"
        case "Cloud Glider":
            return "app\media\gliders\Cloud_Glider.png"
        case "Flower Glider":
            return "app\media\gliders\FlowerGliderMK8.png"
        case "Gold Glider":
            return "app\media\gliders\GoldGliderMK8.png"
        case "Hylian Kite":
            return "app\media\gliders\MK8-HylianKite.png"
        case "Paraglider":
            return "app\media\gliders\MK8D_Paraglider.png"
        case "MKTV Parafoil":
            return "app\media\gliders\MKTVParafoilGliderMK8.png"
        case "Paper Glider":
            return "app\media\gliders\PaperGliderIcon-MK8.png"
        case "Parachute":
            return "app\media\gliders\ParachuteGliderMK8.png"
        case "Parafoil":
            return "app\media\gliders\ParafoilGliderMK8.png"
        case "Peach Parasol":
            return "app\media\gliders\PeachParasolGliderMK8.png"
        case "Plane Glider":
            return "app\media\gliders\PlaneGliderMK8.png"
        case "Super Glider":
            return "app\media\gliders\SuperGliderMK8.png"
        case "Waddle Wing":
            return "app\media\gliders\WaddleWingMK8.png"
        case "Wario Wing":
            return "app\media\gliders\WarioWingMK8.png"

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

# initial calls to main
makeLists([], [])
randomize()
randomizeTrack()
currCharacter = getCurrentCharacter()
currTrack = getCurrentTrack()
currKart = getCurrentKart()
currTire = getCurrentTire()
currGlider = getCurrentGlider()

char_icon = get_char_icon(currCharacter)
kart_icon = get_kart_icon(currKart)
tire_icon = get_tire_icon(currTire)
glider_icon = get_glider_icon(currGlider)
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
