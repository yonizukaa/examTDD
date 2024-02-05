import unittest
from tkinter import Tk,Canvas
from interface.chess_gui import ChessGUI


class TestChessGUI(unittest.TestCase):
    def test_chess_gui_creation(self):
        root = Tk()
        chess_gui = ChessGUI(root)
        self.assertIsNotNone(chess_gui)

    # Simule un clic sur la case (0, 0) du plateau
        chessboard_canvas.event_generate("<Button-1>", x=0, y=0)
        
   # TO DO
if __name__ == "__main__":
    unittest.main()
