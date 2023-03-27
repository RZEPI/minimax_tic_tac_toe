import PySimpleGUI as sg

def init_window():
    layout = []
    for row in range(3):
        row_list = []
        for col in range(3):
            row_list.append(sg.Button(key="{0},{1}".format(row, col), button_color="grey", size=(15,10), border_width=1))
        layout.append(row_list)
    new_window = sg.Window('Minimax', layout)
    return new_window

sg.theme('DarkBlack')

layout = [  
    [sg.Text('TEST')],
    [sg.Button('Start')]
]
window = sg.Window('Choise', layout=layout)

while True:
    event, values = window.read()
    if event == 'Start':
        window = init_window()
    if event == sg.WIN_CLOSED:
        break

window.close()