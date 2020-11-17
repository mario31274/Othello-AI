from src.ui.util import update_ui, x_y_to_row_column
from src.ui.config import board_width, board_height
import src.ui.mainFrame as mainFrame

def onClickBoard(event):
    try:
        mainFrame.board.placePieceAt(x_y_to_row_column(event.x, event.y))
    except Exception as identifier:
        print(identifier)
    update_ui()
