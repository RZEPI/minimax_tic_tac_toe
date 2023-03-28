import constants
class Game:
    def init_board(self):
        board = []
        for _ in range(self._board_size[0]):
            row = []
            for _ in range(self._board_size[1]):
                row.append(None)
            board.append(row)
        self._board = board


    def __init__(self, board_size, win_condition):
        self._board_size = board_size
        self._win_condition = win_condition
        self._active_player = constants.PLAYER_X
