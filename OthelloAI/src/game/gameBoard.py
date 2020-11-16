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
            self.__board = board
        else:
            self.__board = INIT_BOARD
    
    def getGameBoard(self):
        return self.__board

    def getColor(self, position):
        row, col = position
        if row < 1 or row > 8:
            raise IndexError("getColor Error: Invalid row number {}".format(row))
        if col < 1 or col > 8:
            raise IndexError("getColor rror: Invalid column number {}".format(col))
        if self.__board[row-1][col-1] == 1:
            return 'black'
        elif self.__board[row-1][col-1] == -1:
            return 'white'
        else:
            return None
    
    def setColor(self, color, position):        
        row, col = position
        if row < 1 or row > 8:
            raise IndexError("setColor Error: Invalid row number {}".format(row))
        if col < 1 or col > 8:
            raise IndexError("setColor Error: Invalid column number {}".format(col))
        if color == 'black':
            self.__board[row-1][col-1] = 1
        elif color == 'white':
            self.__board[row-1][col-1] = -1
        else:
            raise ValueError("setColor Error: Invalid color: {}".format(color))

    def doAction(self, action, position):
        if self.getColor(position) != None:
            raise "doAction Error: Position " + position + " already occupied."
        if action == 'black':
            self.setColor('black', position)
        elif action == 'white':
            self.setColor('white', position)
        else:
            raise "Error: Invalid action"
        self.updateGameBoard(position)

    def updateGameBoard(self, position):
        pass
            
