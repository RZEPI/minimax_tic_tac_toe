import constants as con
import Point as pt 

class Game:


    def __init__(self, window, board_size, win_condition=3):
        self.__window = window
        self.__board_size = board_size
        self.__win_condition = win_condition
        self.__active_player = con.PLAYER_X
        self.__board = self.init_board()
        self.__turn = {con.PLAYER_X: 0, con.PLAYER_O: 0}


    def init_board(self):
        board = []
        for _ in range(self.__board_size[0]):
            row = []
            for _ in range(self.__board_size[1]):
                row.append(None)
            board.append(row)
        return board


    def place_sign(self, position):
        button = self.__window[position]
        button.update(self.__active_player)
        button.Key = f"l{position}"
        position = self.parse_position(position)
        self.__board[position.row()][position.col()] = self.__active_player
        self.check_win(position)

    
    def parse_position(self, position):
        position = position.split(',')
        for i, cord in enumerate(position):
            position[i] = int(cord)
        position = pt.Point(position[0], position[1])
        return position
    

    def check_row(self, row):
        counter = 0

        if self.__board_size[1] < self.__win_condition:
            return False

        for i in range(self.__board_size[1]):
            if self.__board[row][i] == self.__active_player:
                counter += 1
            else:
                counter = 0
            if counter >= self.__win_condition:
                return True
            
        return False

    def check_col(self, col):
        counter = 0

        if self.__board_size[0] < self.__win_condition:
            return False

        for i in range(self.__board_size[0]):
            if self.__board[i][col] == self.__active_player:
                counter += 1
            else:
                counter = 0
            if counter >= self.__win_condition:
                return True
            
        return False


    def check_diag_l(self, position):
        counter = 1 
        diag_l = pt.Point(position.row(), position.col())
        diag_r = pt.Point(position.row(), position.col())
        move_l = position.row() != 0 and position.col() != 0
        move_r = position.check_in_bounds((0,0), self.__board_size)

        while move_l or move_r:
            if move_l:
                diag_l.dec()
                if self.__board[diag_l.row()][diag_l.col()] == self.__active_player:
                    counter += 1
                    move_l = diag_l.check_in_bounds((0,0), self.__board_size)
                else:
                    move_l = False
            if move_r:
                diag_r.inc()
                if self.__board[diag_r.row()][diag_r.col()] == self.__active_player:
                    counter += 1
                    move_r = diag_r.check_in_bounds((0,0), self.__board_size)
                else:
                    move_r = False
            if counter >= self.__win_condition:
                return True

        return False




    def check_win(self, position):
        if self.check_row(position.row()):
            self.win()
        if self.check_col(position.col()):
            self.win()
        if self.check_diag_l(position):
            self.win()


    #TODO: make win popup
    def win(self):
        print(f"Player {self._active_player} wins!!!")