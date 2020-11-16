import unittest
from src.game.gameState import GameState

class GameStateTests(unittest.TestCase):
    def test_constructor(self):
        gs = GameState()        
        self.assertEqual(gs.getGameState(), 
        [[0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, -1, 0, 0, 0],
        [0, 0, 0, -1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]])

    def test_setColor_outOfRangeError(self):
        gs = GameState()
        self.assertRaises(IndexError, gs.setColor, 'black', (0,0))

    def test_setColor_colorError(self):
        gs = GameState()
        self.assertRaises(ValueError, gs.setColor, None, (1,1))

    def test_doAction(self):
        gs = GameState()
        gs.doAction('black', (3,5))
        self.assertEqual(gs.getGameState(), 
        [[0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 0, 0],
        [0, 0, 0, -1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]])

    def test_doAction_noflip(self):        
        gs = GameState()
        self.assertRaises(Exception, gs.doAction, 'black', (1,1))

    def test_getSuccessors(self):
        gs = GameState()

    def test_setGameState(self):
        st = [[0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 0, 0, 0],
            [0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 0, -1, 1, 0, 0, 0],
            [1, -1, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]]
        gs = GameState()
        gs.setGameState(st)
        self.assertEqual(gs.getGameState(), st)

    def test_GameState_init_sizeError(self):
        st = [[0, 0, 0, 0, 0, 0, 0  ]]
        self.assertRaises(Exception, GameState, st)        

if __name__ == '__main__':
    unittest.main()