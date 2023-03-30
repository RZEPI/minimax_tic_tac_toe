import Game
class GamePvP(Game.Game):
    def __init__(self, window, board_size, win_condition):
        super().__init__(window, board_size, win_condition)


    def change_player(self):
        if self._active_player == Game.constants.PLAYER_X:
            self._active_player = Game.constants.PLAYER_O
        else:
            self._active_player = Game.constants.PLAYER_X
    
            
    def make_move(self, position):
        self.place_sign(position)
        self.change_player()