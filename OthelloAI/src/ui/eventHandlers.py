from src.ui.util import draw_board, x_y_to_row_column
from src.ui.config import board_width, board_height
import src.ui.mainFrame as mainFrame

def onClickBoard(event):
    try:
        mainFrame.board.placePieceAt(x_y_to_row_column(event.x, event.y))
    except Exception as identifier:
        print(identifier)
    draw_board(mainFrame.board_canvas)
    print(mainFrame.board.getCurrentPlayer())

