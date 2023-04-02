import Game
class GamePvP(Game.Game):
    def __init__(self, window, board_size, win_condition=3):
        super().__init__(window, board_size, win_condition)


    def change_player(self):
        if self.__active_player == Game.con.PLAYER_X:
            self.__active_player = Game.con.PLAYER_O
        else:
            self.__active_player = Game.con.PLAYER_X
    
            
    def make_move(self, position):
        self.place_sign(position)
        self.change_player()