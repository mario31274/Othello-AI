from src.singleton import Singleton

class GameBoard(metaclass=Singleton):
    def __init__(self, board = None):
        if board == None:
            self._board = [[0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 1, -1, 0, 0, 0],
                           [0, 0, 0, -1, 1, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0]]
        else:
            self._board = board
    
    def getGameBoard(self):
        return self._board
            
