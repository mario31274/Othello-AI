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
        self.__currentPlayer = 1        # 1 = black, 0 = white
    
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

    def placePieceAt(self, position):
        if self.getColor(position) != None:
            raise Exception("placePieceAt Error: Position {} already occupied.".format(position))
        if self.__currentPlayer == 1:
            self.setColor('black', position)
            self.updateGameBoard(position)
            self.__currentPlayer ^= 1
        elif self.__currentPlayer == 0:
            self.setColor('white', position)
            self.updateGameBoard(position)
            self.__currentPlayer ^= 1
        else:
            raise Exception("Error: Invalid action")

    def updateGameBoard(self, position):
        pass

    def isValidMove(self, position):
        pass

    def getCurrentPlayer(self):
        if self.__currentPlayer == 1:
            return "black"
        else:
            return "white"