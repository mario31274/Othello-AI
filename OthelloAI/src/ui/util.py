import math
import tkinter as tk
from src.ui.config import *
import src.ui.mainFrame as mainFrame

def draw_gridlines(canvas):
    for i in range(8):
        x = board_width/8 * i
        canvas.create_line(x, 0, x, board_height)
    canvas.create_line(board_width-1, 0, board_width-1, board_height)
    for i in range(8):
        y = board_height/8 * i
        canvas.create_line(0, y, board_width, y)
    canvas.create_line(0, board_height-1, board_width, board_height-1)

def draw_piece(canvas, row, col, color):
    if color != None:
        x1 = board_width/8 * (row-1) + piece_border
        y1 = board_height/8 * (col-1) + piece_border
        x2 = board_width/8 * (row) - piece_border
        y2 = board_height/8 * (col) - piece_border
        canvas.create_oval(x1, y1, x2, y2, fill=color, outline=color)    

def draw_board(canvas):    
    for row in range(1, 9):
        for col in range(1, 9):
            draw_piece(canvas, row, col, mainFrame.board.getColor((row, col)))

def x_y_to_row_column(x, y):
    width = (board_width-2) / 8
    height = (board_height-2) / 8
    row = math.floor(x / width) + 1
    col = math.floor(y / height) + 1
    return (row, col)

def update_ui(canvas):
    pass