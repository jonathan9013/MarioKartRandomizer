from tkinter import TOP
import PySimpleGUI as gui
from main import *
from Track import Track
from Character import Character
from Cup import Cup
from kart import Kart
from glider import Glider
from tire import Tire

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
randomizeCup()

# get info from backend
currCharacter = getCurrentCharacter()
currTrack = getCurrentTrack()
currKart = getCurrentKart()
currTire = getCurrentTire()
currGlider = getCurrentGlider()
currCup = getCurrentCup()

# call case match functions to get correct file paths
char_icon = currCharacter.image
kart_icon = currKart.image
tire_icon = currTire.image
glider_icon = currGlider.image
track_icon1 = currTrack.image
cup_icon = currCup.image

track_cup_text1 = currTrack.cup

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
                [gui.Button(key='-REROLLTRACK1-', image_filename=r'app\media\refresh_icon.png', border_width=0, button_color='#a8cfdd', mouseover_colors='#a8cfdd'), gui.Text(track_cup_text1, key="track_cup1")] # TODO - display track's Cup property here
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
        kart_icon = currKart.image

        element = window[event]
        window['kart_image'].update(filename=kart_icon)

    if event == '-REROLLTIRE-':
        randomizeAspect("tires")
        currTire = getCurrentTire()
        tire_icon = currTire.image

        element = window[event]
        window['tire_image'].update(filename=tire_icon)

    if event == '-REROLLGLIDER-':
        randomizeAspect("glider")
        currGlider = getCurrentGlider()
        glider_icon = currGlider.image

        element = window[event]
        window['glider_image'].update(filename=glider_icon)

    if event == '-REROLLTRACK1-':
        randomizeTrack(True)
        currTrack = getCurrentTrack()
        track_icon = currTrack.image
        track_cup_text = currTrack.cup

        window['track_image1'].update(filename=track_icon)
        window['track_cup1'].update(track_cup_text)

    if event == '-GENERATETRACK-':
        # numberOfTracks = gui.popup_get_text('Enter the number of tracks you would like to generate: ', keep_on_top=True)
        # if numberOfTracks != None:
        # numberOfTracks = int(numberOfTracks)
        randomizeTrack(False)
        currTrack = getCurrentTrack()
        track_icon = currTrack.image
        track_cup_text = currTrack.cup

        window['track_image1'].update(filename=track_icon)
        window['track_cup1'].update(track_cup_text)
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
            kart_icon = currKart.image

            currTire = getCurrentTire()
            tire_icon = currTire.image

            currGlider = getCurrentGlider()
            glider_icon = currGlider.image

            window['char_image'].update(filename=char_icon)
            window['kart_image'].update(filename=kart_icon)
            window['tire_image'].update(filename=tire_icon)
            window['glider_image'].update(filename=glider_icon)

    if event == '-GENERATECUP-':
        randomizeCup()
        cup = getCurrentCup()

        window['cup_image'].update(filename=cup.image)

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
