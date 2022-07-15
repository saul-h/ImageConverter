from PIL import Image
import os.path
import PySimpleGUI as sg

fileList = [
    [
        sg.Text('Image:'),
        sg.In(size = (25, 1), enable_events = True, key = '-FOLDER-'),
        sg.FolderBrowse(),
    ],
    [
        sg.Listbox(
            values = [], enable_events = True, size = (40, 20), key = '-FILE LIST-'
        )
    ],
]

convertImage = [
    [
        sg.Text('Convert: '),
        sg.Text(size=(40, 1), key='-IMAGE PATH-')
    ],
    [
        sg.Text('To: '),
        sg.DropDown(
            ['Select an Image'], enable_events = False, key='-IMAGE FORMAT-'
        )
    ],
    [
        sg.Image(key='-IMAGE PREVIEW-')
    ],
    [
        sg.SaveAs(key='-SAVE BUTTON-')
    ],
]

layout = [
    [
        sg.Column(fileList),
        sg.VSeperator(),
        sg.Column(convertImage),
    ]
]

window = sg.Window('Image Converter', layout)

while True:
    event, values = window.read()
    if event == 'Exit' or event == sg.WIN_CLOSED:
        break
    if event == 
