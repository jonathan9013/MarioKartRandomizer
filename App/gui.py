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


gui.theme("LightBlue3") # set theme

makeLists([], [])
randomize()
currCharacter = getCurrentCharacter()

char_icon = get_char_icon(currCharacter)
kart_icon = 'app\media\karts\Gold_Standard.png'
tire_icon = 'app\media\\tires\Gold_Tires_MK8.png'
glider_icon = 'app\media\gliders\GoldGliderMK8.png'
track_icon = 'app\media\\tracks\MK8_Rainbow_Road_Course_Icon.png'

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
