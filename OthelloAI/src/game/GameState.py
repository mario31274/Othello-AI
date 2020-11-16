from src.game.gameBoard import INIT_BOARD

class GameState:
    def __init__(self, state = None):
        if state != None:
            if len(state) != 8:
                raise Exception("init Error: Board size error")
            for l in state:
                if len(l) != 8:
                    raise Exception("init Error: Board size error")
            self.data = state
        else:
            self.data = INIT_BOARD
            
    def setGameState(self, state):
        if len(state) != 8:
            raise Exception("init Error: Board size error")
        for l in state:
            if len(l) != 8:
                raise Exception("init Error: Board size error")
        self.data = state


    def getGameState(self):
        return self.data

    def getColor(self, position):
        row, col = position
        if row < 1 or row > 8:
            raise IndexError("getColor Error: Invalid row number {}".format(row))
        if col < 1 or col > 8:
            raise IndexError("getColor rror: Invalid column number {}".format(col))
        if self.data[row-1][col-1] == 1:
            return 'black'
        elif self.data[row-1][col-1] == -1:
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
            self.data[row-1][col-1] = 1
        elif color == 'white':
            self.data[row-1][col-1] = -1
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
        self.updateGameState(position)

    def updateGameState(self, position):
        pass

    def getSussessors(self):
        pass


        
    