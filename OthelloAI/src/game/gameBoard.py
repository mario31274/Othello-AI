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
            raise IndexError("getColor Error: Invalid column number {}".format(col))
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

    def getPieceNumbers(self):
        black_number = white_number = 0
        for row in self.__board:
            for piece in row:
                if piece == 1:
                    black_number += 1
                elif piece == -1:                    
                    white_number += 1
        return black_number, white_number

    def placePieceAt(self, position):
        if self.getColor(position) != None:
            raise Exception("placePieceAt Error: Position {} already occupied.".format(position))
        if position in self.getValidMoves():
            if self.__currentPlayer == 1:
                self.setColor('black', position)
                self.updateGameBoard(position)
                self.__currentPlayer ^= 1
            elif self.__currentPlayer == 0:
                self.setColor('white', position)
                self.updateGameBoard(position)
                self.__currentPlayer ^= 1
        else:
            raise Exception("Error: Invalid move")

    def updateGameBoard(self, position):
        row, col = position
        self.__flipLine(row, col, -1,  0)
        self.__flipLine(row, col, -1,  1)
        self.__flipLine(row, col,  0,  1)
        self.__flipLine(row, col,  1,  1)
        self.__flipLine(row, col,  1,  0)
        self.__flipLine(row, col,  1, -1)
        self.__flipLine(row, col,  0, -1)
        self.__flipLine(row, col, -1, -1)

    def isValidMove(self, position, drow, dcol):
        if self.__currentPlayer == 1:
            other = "white"
        elif self.__currentPlayer == 0:
            other = "black"
        else:
            raise RuntimeError("__currentPlayer Error")

        row, col = position
        if not 1 <= row+drow <= 8:
            return False
        if not 1 <= col+dcol <= 8:
            return False
        if self.getColor((row+drow, col+dcol)) != other:
            return False
        
        if not 1 <= row+drow+drow <= 8:
            return False
        if not 1 <= col+dcol+dcol <= 8:
            return False
        return self.__checkLine(row+drow+drow, col+dcol+dcol, drow, dcol)

    def getCurrentPlayer(self):
        if self.__currentPlayer == 1:
            return "black"
        else:
            return "white"

    def getValidMoves(self):
        valid = list()
        nn = ne = ee = se = ss = sw = ww = nw = False
        for row in range(1,9):
            for col in range(1,9):
                if self.getColor((row, col)) == None:
                    nn = self.isValidMove((row, col), -1,  0)
                    ne = self.isValidMove((row, col), -1,  1)
                    ee = self.isValidMove((row, col),  0,  1)
                    se = self.isValidMove((row, col),  1,  1)
                    ss = self.isValidMove((row, col),  1,  0)
                    sw = self.isValidMove((row, col),  1, -1)
                    ww = self.isValidMove((row, col),  0, -1)
                    nw = self.isValidMove((row, col), -1, -1)
                if (nn or ne or ee or se or ss or sw or ww or nw) and self.getColor((row, col)) == None:
                    valid.append((row, col))
        return valid

    def __checkLine(self, row, col, drow, dcol):
        if self.getColor((row, col)) == self.getCurrentPlayer():
            return True
        if not 1 <= row+drow <= 8:
            return False
        if not 1 <= col+dcol <= 8:
            return False
        return self.__checkLine(row+drow, col+dcol, drow, dcol)

    def __flipLine(self, row, col, drow, dcol):
        if not 1 <= row+drow <= 8:
            return False
        if not 1 <= col+dcol <= 8:
            return False
        if self.getColor((row+drow, col+dcol)) == None:
            return False

        if self.getColor((row+drow, col+dcol)) == self.getCurrentPlayer():
            return True
        else:
            if self.__flipLine(row+drow, col+dcol, drow, dcol):
                self.setColor(self.getCurrentPlayer(), (row+drow, col+dcol))
                # print('flipped')
                return True
            else:
                return False
            
