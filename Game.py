import constants
class Game:

    def __init__(self, window, board_size, win_condition):
        self._window = window
        self._board_size = board_size
        self._win_condition = win_condition
        self._active_player = constants.PLAYER_X
        self._board = self.init_board()


    def init_board(self):
        board = []
        for _ in range(self._board_size[0]):
            row = []
            for _ in range(self._board_size[1]):
                row.append(None)
            board.append(row)
        return board


    def place_sign(self, position):
        button = self._window[position]
        button.update(self._active_player)
        button.Key = f"l{position}"
        position = self.parse_position(position)
        self._board[position[0]][position[1]] = self._active_player

    
    def parse_position(self, position):
        position = position.split(',')
        for i, cord in enumerate(position):
            position[i] = int(cord)
        return position
    
