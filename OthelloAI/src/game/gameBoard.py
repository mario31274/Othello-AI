from src.singleton import Singleton

INIT_BOARD = [[0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 1, -1, 0, 0, 0],
              [0, 0, 0, -1, 1, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0]]

class GameBoard(metaclass=Singleton):
    def __init__(self, board = None):
        if board != None:
            if len(board) != 8:
                raise Exception("init Error: Board size error")
            for l in board:
                if len(l) != 8:
                    raise Exception("init Error: Board size error")
            self._board = board
        else:
            self._board = INIT_BOARD
    
    def getGameBoard(self):
        return self._board
            
