import tkinter as tk
from src.ui.util import draw_gridlines, draw_board
from src.ui.config import *
from src.game.gameBoard import GameBoard
from src.ui.eventHandlers import onClickBoard

root = tk.Tk()
root.title("Othello v0.1")
root.configure(background='green')
board_frame = tk.Frame(root, background='green')
board_frame.pack()

board_canvas = tk.Canvas(board_frame, width=window_width, height=window_height, background='green', borderwidth=0, highlightthickness=0)
row_num_canvas = tk.Canvas(board_frame, width=row_num_width, height=row_num_height, background='green', borderwidth=0, highlightthickness=0)
col_num_canvas = tk.Canvas(board_frame, width=col_num_width, height=col_num_height, background='green', borderwidth=0, highlightthickness=0)
board_canvas.grid(row=1, column=1)
row_num_canvas.grid(row=1, column=0)
col_num_canvas.grid(row=0, column=1)
draw_gridlines(board_canvas)

board = GameBoard()
draw_board(board_canvas)

board_canvas.bind("<Button-1>", onClickBoard)
