from tkinter import TOP
import PySimpleGUI as gui
from main import *
from Track import Track
from Character import Character

# TODO - REMOVE THESE
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

def check_valid(type_array, size_array):
    kart_exists = False
    size_exists = False
    karts = []
    sizes = []

    for element, flag in type_array:
        if flag == True:
            kart_exists = True
            karts.append(element)

    for element, flag in size_array:
        if flag == True:
            size_exists = True
            sizes.append(element)

    if kart_exists and size_exists:
        return True, sizes, karts
    else:
        return False, [], []

gui.theme("LightBlue3") # set theme

# initial calls to main
initialize()
makeLists(['Light', 'Medium', 'Heavy'], ['Karts', 'Standard Bikes', 'Sport Bikes', 'ATVs'])
randomize()
randomizeTrack(False)

# get info from backend
currCharacter = getCurrentCharacter()
currTrack = getCurrentTrack()
currKart = getCurrentKart()
currTire = getCurrentTire()
currGlider = getCurrentGlider()

# call case match functions to get correct file paths
char_icon = currCharacter.image
kart_icon = get_kart_icon(currKart)
tire_icon = get_tire_icon(currTire)
glider_icon = get_glider_icon(currGlider)
track_icon1 = currTrack.image
cup_icon = 'app\media\cups\MK8D_BCP_Golden_Dash_Emblem.png' # TODO - get icon from backend

left_column = [
    [
        gui.Button(key='-REROLLCHAR-', image_filename=r'app\media\refresh_icon.png', border_width=0, button_color='#a8cfdd', mouseover_colors='#a8cfdd', pad=((10,5),(3,3))),
        gui.Image(filename=char_icon, key='char_image', pad=((56,35),(10,10))),
        gui.Text('Character', font=('Helvetica', 12, 'bold')),
    ],
    [
        gui.Button(key='-REROLLKART-', image_filename=r'app\media\refresh_icon.png', border_width=0, button_color='#a8cfdd', mouseover_colors='#a8cfdd', pad=((10, 5),(3, 3))),
        gui.Image(filename=kart_icon, key='kart_image', pad=((20,15),(10,10))),
        gui.Text('Kart', font=('Helvetica', 12, 'bold')),
    ],
    [
        gui.Button(key='-REROLLTIRE-', image_filename=r'app\media\refresh_icon.png', border_width=0, button_color='#a8cfdd', mouseover_colors='#a8cfdd', pad=((10,5),(3,3))),
        gui.Image(filename=tire_icon, key='tire_image', pad=((20,15),(10,10))),
        gui.Text('Tire', font=('Helvetica', 12, 'bold')),
    ],
    [
        gui.Button(key='-REROLLGLIDER-', image_filename=r'app\media\refresh_icon.png', border_width=0, button_color='#a8cfdd', mouseover_colors='#a8cfdd', pad=((10,5),(3,3))),
        gui.Image(filename=glider_icon, key='glider_image', pad=((20,15),(10,10))),
        gui.Text('Glider', font=('Helvetica', 12, 'bold')),
    ],
    [gui.Button('Generate Loadout', key='-GENLOADOUT-', mouseover_colors='#183440', pad=((10,5),(20,20)))],
    [
        gui.Checkbox("Karts", default = True, font=('Helvetica', 10), key='-KARTCHECK-'),
        gui.Checkbox("Standard Bikes", default = True, font=('Helvetica', 10), key='-BIKECHECK-'),
        gui.Checkbox("Sport Bikes", default = True, font=('Helvetica', 10), key='-SPORTCHECK-'),
        gui.Checkbox("ATVs", default = True, font=('Helvetica', 10), key='-ATVCHECK-'),
        gui.Button("Enable all", font=('Helvetica', 10), key='-ALLKARTCHECK-', mouseover_colors='#183440'),
    ],
    [
        gui.Checkbox("Light", default = True, font=('Helvetica', 10), key='-LIGHTCHECK-'),
        gui.Checkbox("Medium", default = True, font=('Helvetica', 10), key='-MEDCHECK-'),
        gui.Checkbox("Heavy", default = True, font=('Helvetica', 10), key='-HEAVYCHECK-'),
        gui.Button("Enable all", font=('Helvetica', 10),  key='-ALLSIZECHECK-', mouseover_colors='#183440')
    ],
]

right_column = [
    # first row of tracks
    [
        gui.Column(
            layout=[
                [gui.Image(filename=track_icon1, key='track_image1')], # TODO - change filename
                [gui.Button(key='-REROLLTRACK1-', image_filename=r'app\media\refresh_icon.png', border_width=0, button_color='#a8cfdd', mouseover_colors='#a8cfdd'), gui.Text("Shell Cup")] # TODO - display track's Cup property here
            ],
            pad=((0,20),(5,5))
        ),
        gui.Column(
            layout=[
                [gui.Image(filename=track_icon1, key='track_image2')], # TODO - change filename
                [gui.Button(key='-REROLLTRACK2-', image_filename=r'app\media\refresh_icon.png', border_width=0, button_color='#a8cfdd', mouseover_colors='#a8cfdd'), gui.Text("Mushroom Cup")] # TODO - display track's Cup property here
            ],
            pad=((0,20),(5,5))
        ),
        gui.Column(
            layout=[
                [gui.Image(filename=track_icon1, key='track_image3')], # TODO - change filename
                [gui.Button(key='-REROLLTRACK3-', image_filename=r'app\media\refresh_icon.png', border_width=0, button_color='#a8cfdd', mouseover_colors='#a8cfdd'), gui.Text("Banana Cup")] # TODO - display track's Cup property here
            ],
            pad=((0,20),(5,5))
        ),
        gui.Column(
            layout=[
                [gui.Image(filename=track_icon1, key='track_image4')], # TODO - change filename
                [gui.Button(key='-REROLLTRACK4-', image_filename=r'app\media\refresh_icon.png', border_width=0, button_color='#a8cfdd', mouseover_colors='#a8cfdd'), gui.Text("Golden Dash Cup")] # TODO - display track's Cup property here
            ],
            pad=((0,20),(5,5))
        ),
    ],

    # second row of tracks
    [
        gui.Column(
            layout=[
                [gui.Image(filename=track_icon1, key='track_image5')], # TODO - change filename
                [gui.Button(key='-REROLLTRACK5-', image_filename=r'app\media\refresh_icon.png', border_width=0, button_color='#a8cfdd', mouseover_colors='#a8cfdd'), gui.Text("Propeller Cup")] # TODO - display track's Cup property here
            ],
            pad=((0,20),(5,5))
        ),
        gui.Column(
            layout=[
                [gui.Image(filename=track_icon1, key='track_image6')], # TODO - change filename
                [gui.Button(key='-REROLLTRACK6-', image_filename=r'app\media\refresh_icon.png', border_width=0, button_color='#a8cfdd', mouseover_colors='#a8cfdd'), gui.Text("Lightning Cup")] # TODO - display track's Cup property here
            ],
            pad=((0,20),(5,5))
        ),
        gui.Column(
            layout=[
                [gui.Image(filename=track_icon1, key='track_image7')], # TODO - change filename
                [gui.Button(key='-REROLLTRACK7-', image_filename=r'app\media\refresh_icon.png', border_width=0, button_color='#a8cfdd', mouseover_colors='#a8cfdd'), gui.Text("Leaf Cup")] # TODO - display track's Cup property here
            ],
            pad=((0,20),(5,5))
        ),
        gui.Column(
            layout=[
                [gui.Image(filename=track_icon1, key='track_image8')], # TODO - change filename
                [gui.Button(key='-REROLLTRACK8-', image_filename=r'app\media\refresh_icon.png', border_width=0, button_color='#a8cfdd', mouseover_colors='#a8cfdd'), gui.Text("Egg Cup")] # TODO - display track's Cup property here
            ],
            pad=((0,20),(5,5))
        ),
    ],
    [gui.Button('Generate Track(s)', key='-GENERATETRACK-', mouseover_colors='#183440', pad=((5,5),(20,20)))],
	[
        gui.Text("Number Of Tracks Before Reset: "),
        gui.InputText('4', size=(5,1), key="resetInput"),
        gui.Button('Apply', key="_setTrackReset_", mouseover_colors='#183440')
    ],
	[
        gui.Text("Current number of tracks before reset:"),
        gui.Text(getTrackReset(), key="track_reset")
    ],
    [
        gui.Image(filename=cup_icon, key='cup_image', pad=((5,15),(30,10))),
        gui.Button('Generate Cup', key="-GENERATECUP-", mouseover_colors='#183440', pad=((5,5),(30,10)))
    ],
]

layout = [
    [
        gui.Column(left_column, vertical_alignment=TOP),
        gui.VSeparator(),
        gui.Column(right_column, vertical_alignment=TOP)
    ],
]

# Create the Window
window = gui.Window('Mario Kart 8 Deluxe Randomizer', layout, resizable=True, icon='App\media\window_icon.ico').Finalize()

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == gui.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    if event == '-REROLLCHAR-':
        randomizeAspect("character")
        currCharacter = getCurrentCharacter()
        char_icon = currCharacter.image

        element = window[event]
        window['char_image'].update(filename=char_icon)

    if event == '-REROLLKART-':
        randomizeAspect("kart")
        currKart = getCurrentKart()
        kart_icon = get_kart_icon(currKart)

        element = window[event]
        window['kart_image'].update(filename=kart_icon)

    if event == '-REROLLTIRE-':
        randomizeAspect("tires")
        currTire = getCurrentTire()
        tire_icon = get_tire_icon(currTire)

        element = window[event]
        window['tire_image'].update(filename=tire_icon)

    if event == '-REROLLGLIDER-':
        randomizeAspect("glider")
        currGlider = getCurrentGlider()
        glider_icon = get_glider_icon(currGlider)

        element = window[event]
        window['glider_image'].update(filename=glider_icon)

    if event == '-REROLLTRACK1-':
        randomizeTrack(True)
        currTrack = getCurrentTrack()
        track_icon = currTrack.image

        element = window[event]
        window['track_image1'].update(filename=track_icon)

    if event == '-GENERATETRACK-':
        # numberOfTracks = gui.popup_get_text('Enter the number of tracks you would like to generate: ', keep_on_top=True)
        # if numberOfTracks != None:
        # numberOfTracks = int(numberOfTracks)
        randomizeTrack(False)
        currTrack = getCurrentTrack()
        track_icon = currTrack.image

        element = window[event]
        window['track_image1'].update(filename=track_icon)
        window['track_reset'].update(getTrackReset())

    if event == '-GENLOADOUT-':
        type_array = [
                (window['-KARTCHECK-'].Text, values["-KARTCHECK-"]),
                (window['-BIKECHECK-'].Text, values["-BIKECHECK-"]),
                (window['-SPORTCHECK-'].Text, values["-SPORTCHECK-"]),
                (window['-ATVCHECK-'].Text, values["-ATVCHECK-"])
            ]
        size_array = [
                (window['-LIGHTCHECK-'].Text, values["-LIGHTCHECK-"]),
                (window['-MEDCHECK-'].Text, values["-MEDCHECK-"]),
                (window['-HEAVYCHECK-'].Text, values["-HEAVYCHECK-"])
            ]

        flag, size_array, type_array = check_valid(type_array, size_array)

        if(not flag):
            gui.Popup('Select at least 1 kart and 1 character type.', keep_on_top=True)
        else:
            makeLists(size_array, type_array)

            randomize()

            currCharacter = getCurrentCharacter()
            char_icon = currCharacter.image

            currKart = getCurrentKart()
            kart_icon = get_kart_icon(currKart)

            currTire = getCurrentTire()
            tire_icon = get_tire_icon(currTire)

            currGlider = getCurrentGlider()
            glider_icon = get_glider_icon(currGlider)

            window['char_image'].update(filename=char_icon)
            window['kart_image'].update(filename=kart_icon)
            window['tire_image'].update(filename=tire_icon)
            window['glider_image'].update(filename=glider_icon)

    if event == '-GENERATECUP-':
        # TODO - get updated cup icon from backend
        window['cup_image'].update(filename=cup_icon)

    if event == '-ALLKARTCHECK-':
        window['-KARTCHECK-'].update(True)
        window['-BIKECHECK-'].update(True)
        window['-SPORTCHECK-'].update(True)
        window['-ATVCHECK-'].update(True)

    if event == '-ALLSIZECHECK-':
        window['-LIGHTCHECK-'].update(True)
        window['-MEDCHECK-'].update(True)
        window['-HEAVYCHECK-'].update(True)

    if event == "_setTrackReset_":
        setTrackReset(int(values["resetInput"]))
        window['track_reset'].update(getTrackReset())

window.close()
