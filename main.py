import PySimpleGUI as sg
import Gameai
import Gamepvp
import Game


def init_window(size):
    layout = []
    for row in range(size[0]):
        row_list = []
        for col in range(size[1]):
            row_list.append(sg.Button(key=f"{row},{col}", button_color="grey", size=(20,10), border_width=1))
        layout.append(row_list)
    new_window = sg.Window('Minimax', layout)
    return new_window, layout


sg.theme('DarkBlack')

layout = [  
    [sg.Text('TEST')],
    [sg.Button('Start')]
]
window = sg.Window('Tic-Tac-Toe', layout=layout)
size_of_board = (3,3)
while True:
    event, values = window.read()
    if event == 'Start':
        window, layout = init_window(size_of_board)
        game = Gamepvp.GamePvP(window, size_of_board)
    elif event == sg.WIN_CLOSED:
        break
    elif event[0] != "l":
        game.make_move(event)

window.close()