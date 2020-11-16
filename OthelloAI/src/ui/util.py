import tkinter as tk
from .config import *

def draw_gridlines(canvas):
    i = 0
    while i < 8:        
        x = board_width/8 * i
        canvas.create_line(x, 0, x, board_height)
        i = i+1
    i = 0
    while i < 8:        
        y = board_height/8 * i
        canvas.create_line(0, y, board_width, y)
        i = i+1

def draw_white(canvas, row, col):
    x1 = board_width/8 * (row-1) + piece_border
    y1 = board_height/8 * (col-1) + piece_border
    x2 = board_width/8 * (row) - piece_border
    y2 = board_height/8 * (col) - piece_border
    canvas.create_oval(x1, y1, x2, y2, fill="white", outline="white")

def draw_black(canvas, row, col):
    x1 = board_width/8 * (row-1) + piece_border
    y1 = board_height/8 * (col-1) + piece_border
    x2 = board_width/8 * (row) - piece_border
    y2 = board_height/8 * (col) - piece_border
    canvas.create_oval(x1, y1, x2, y2, fill="black", outline="black")

# def _create_circle(self, x, y, r, **kwargs):
#     return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)

# tk.Canvas.create_circle = _create_circle