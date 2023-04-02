class Point:


    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    
    def check_in_bounds(self, start:tuple,end:tuple):
        if self.__x < start[0] and self.__y < start[1]:
            return False
        if self.__x > end[0] and self.__y > end[1]:
            return False
        return True
    

    def dec(self):
        self.__x = self.__x - 1
        self.__y = self.__y - 1


    def inc(self):
        self.__x = self.__x + 1
        self.__y = self.__y + 1


    def row(self):
        return self.__x 
    

    def col(self):
        return self.__y