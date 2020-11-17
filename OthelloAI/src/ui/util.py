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

def draw_row_line_number(canvas):
    for i in range(8):
        x = row_num_width / 2
        y = row_num_height / 8 * (i + 0.25)
        canvas.create_text(x,y,text=i+1, font=(line_number_font, line_number_font_size), fill=line_number_font_color)

def draw_col_line_number(canvas):
    for i in range(8):
        x = col_num_width / 8 * (i + 0.25)
        y = col_num_height / 2
        canvas.create_text(x,y,text=i+1, font=(line_number_font, line_number_font_size), fill=line_number_font_color)

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

def draw_valid_moves(canvas):
    for row, col in mainFrame.board.getValidMoves():
        x1 = board_width/8 * (row-1) + valid_move_border
        y1 = board_height/8 * (col-1) + valid_move_border
        x2 = board_width/8 * (row) - valid_move_border
        y2 = board_height/8 * (col) - valid_move_border
        canvas.create_oval(x1, y1, x2, y2, fill="gray", outline="gray", tags="valid")

def draw_icon(canvas, color):
    x1 = scoreboard_piece_icon_offset
    y1 = (scoreboard_height - scoreboard_piece_icon_size) / 2
    x2 = x1 + scoreboard_piece_icon_size
    y2 = y1 + scoreboard_piece_icon_size
    canvas.create_oval(x1, y1, x2, y2, fill=color, outline=color)

def draw_scoreboard():
    x = scoreboard_piece_icon_offset * 3 + scoreboard_piece_icon_size
    y = scoreboard_piece_icon_size
    black_num, white_num = mainFrame.board.getPieceNumbers()
    mainFrame.scoreboard_black_canvas.delete("score")
    mainFrame.scoreboard_white_canvas.delete("score")
    mainFrame.scoreboard_black_canvas.create_text(x,y,text=black_num, font=(scoreboard_font, scoreboard_font_size), fill=scoreboard_font_color, tags="score")
    mainFrame.scoreboard_white_canvas.create_text(x,y,text=white_num, font=(scoreboard_font, scoreboard_font_size), fill=scoreboard_font_color, tags="score")

def draw_message(label, msg):
    label.config(text=msg)

def x_y_to_row_column(x, y):
    width = (board_width-2) / 8
    height = (board_height-2) / 8
    row = math.floor(x / width) + 1
    col = math.floor(y / height) + 1
    return (row, col)

def update_ui():
    draw_board(mainFrame.board_canvas)
    mainFrame.board_canvas.delete("valid")
    draw_valid_moves(mainFrame.board_canvas)
    if mainFrame.board.isGameOver():
        if mainFrame.board.getWinner() == 1:
            draw_message(mainFrame.message_bar_label, "Black wins!")
        elif mainFrame.board.getWinner() == -1:
            draw_message(mainFrame.message_bar_label, "White wins!")
        else:            
            draw_message(mainFrame.message_bar_label, "It's a tie!")
    else:
        if len(mainFrame.board.getValidMoves()) == 0:
            draw_message(mainFrame.message_bar_label, "{} has no legal moves, \n will skip one turn.".format(mainFrame.board.getCurrentPlayer()))
        else:
            draw_message(mainFrame.message_bar_label, "{}'s turn".format(mainFrame.board.getCurrentPlayer()))
    draw_scoreboard()