import unittest

from chess_board import ChessBoard
from role.bishop import Bishop
from role.king import King
from role.knight import Knight
from role.pawn import Pawn
from role.piece import Piece
from role.queen import Queen
from role.rook import Rook

class TestPiece(unittest.TestCase):
    def test_piece_creation(self):
        piece = Piece('white', ChessBoard(), (0, 0))
        self.assertIsNotNone(piece)

    def test_piece_valid_moves(self):
        board = ChessBoard()
        piece = Piece('white', board, (0, 0))
        self.assertEqual(piece.get_valid_moves(), [])
#pawn
    def test_pawn_valid_moves(self):
        board = ChessBoard()
        pawn = Pawn('white', board, (1, 0))
        
        valid_moves = pawn.get_valid_moves()
        self.assertEqual(valid_moves, [(1, 1), (1, 2)])

    def test_pawn_invalid_moves(self):
        board = ChessBoard()
        pawn = Pawn('white', board, (1, 7))
        
        invalid_moves = pawn.get_valid_moves()
        self.assertEqual(invalid_moves, [])
#king
    def test_king_valid_moves(self):
        board = ChessBoard()
        king = King('white', board, (0, 0))
        self.assertEqual(king.get_valid_moves(), [])

    def test_king_invalid_moves(self):
        board = ChessBoard()
        king = King('white', board, (0, 0))
        
        invalid_moves = king.get_invalid_moves()
        self.assertNotEqual(invalid_moves, [])    
#queen
def test_queen_valid_moves(self):
        board = ChessBoard()
        queen = Queen('white', board, (0, 0))
        self.assertEqual(queen.get_valid_moves(), [])

def test_queen_invalid_moves(self):
        board = ChessBoard()
        queen = Queen('white', board, (0, 0))
        
        invalid_moves = queen.get_invalid_moves()
        self.assertNotEqual(invalid_moves, [])       
#bishop
def test_bishop_valid_moves(self):
        board = ChessBoard()
        bishop = Bishop('white', board, (0, 0))
        self.assertEqual(bishop.get_valid_moves(), []) 

def test_bishop_invalid_moves(self):
        board = ChessBoard()
        bishop = Bishop('white', board, (0, 0))
       
        invalid_moves = bishop.get_invalid_moves()
        self.assertNotEqual(invalid_moves, [])       
#knight
def test_knight_valid_moves(self):
        board = ChessBoard()
        knight = Knight('white', board, (0, 0))
        self.assertEqual(knight.get_valid_moves(), [])     

def test_knight_invalid_moves(self):
        board = ChessBoard()
        knight = Knight('white', board, (0, 0))
        invalid_moves = knight.get_invalid_moves()
        self.assertNotEqual(invalid_moves, [])
   #rook
def test_rook_valid_moves(self):
        board = ChessBoard()
        rook = Rook('white', board, (0, 0))
        self.assertEqual(rook.get_valid_moves(), [])    

def test_rook_invalid_moves(self):
        board = ChessBoard()
        rook = Rook('white', board, (0, 0))
        invalid_moves = rook.get_invalid_moves()
        self.assertNotEqual(invalid_moves, [])             