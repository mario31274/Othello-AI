import tkinter as tk
from src.ui.util import draw_gridlines, draw_row_line_number, draw_col_line_number, draw_icon, update_ui
from src.ui.config import *
from src.game.gameBoard import GameBoard
from src.ui.eventHandlers import onClickBoard

root = tk.Tk()
root.title("Othello v0.1")
root.configure(background='green')
board_frame = tk.Frame(root, background='green')
scoreboard_frame = tk.Frame(root, background='green')
board_frame.pack()
scoreboard_frame.pack(fill='both')

board_canvas = tk.Canvas(board_frame, width=window_width, height=window_height, background='green', borderwidth=0, highlightthickness=0)
row_num_canvas = tk.Canvas(board_frame, width=row_num_width, height=row_num_height, background='green', borderwidth=0, highlightthickness=0)
col_num_canvas = tk.Canvas(board_frame, width=col_num_width, height=col_num_height, background='green', borderwidth=0, highlightthickness=0)
board_canvas.grid(row=1, column=1)
row_num_canvas.grid(row=1, column=0)
col_num_canvas.grid(row=0, column=1)

scoreboard_black_canvas = tk.Canvas(scoreboard_frame, width=scoreboard_score_width, height=scoreboard_height, background='green', borderwidth=0, highlightthickness=0)
scoreboard_white_canvas = tk.Canvas(scoreboard_frame, width=scoreboard_score_width, height=scoreboard_height, background='green', borderwidth=0, highlightthickness=0)
message_bar_label = tk.Label(scoreboard_frame, font=(message_font, message_font_size), foreground=message_font_color, background='green')
scoreboard_black_canvas.pack(side='left')
message_bar_label.pack(side='left', expand=True)
scoreboard_white_canvas.pack(side='right')
draw_gridlines(board_canvas)
draw_row_line_number(row_num_canvas)
draw_col_line_number(col_num_canvas)
draw_icon(scoreboard_black_canvas, 'black')
draw_icon(scoreboard_white_canvas, 'white')

board = GameBoard()
update_ui()

board_canvas.bind("<Button-1>", onClickBoard)
