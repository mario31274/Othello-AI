import tkinter as tk
from src.ui.util import draw_gridlines
from src.ui.config import *
from src.game.gameBoard import GameBoard

root = tk.Tk()
root.title("Othello v0.1")

canvas = tk.Canvas(root, width=window_width, height=window_height, background='green', borderwidth=0, highlightthickness=0)
canvas.grid()
root.configure(background='green')
draw_gridlines(canvas)

board = GameBoard()
print(board.getGameBoard())

# Util._draw_white(canvas, 4, 4)
# Util._draw_black(canvas, 4, 5)
# Util._draw_white(canvas, 5, 5)
# Util._draw_black(canvas, 5, 4)
