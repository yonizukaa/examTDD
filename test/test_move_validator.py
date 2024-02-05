import unittest

from chess_board import ChessBoard
from gameplay.move_validator import MoveValidator
from role.pawn import Pawn


class TestMoveValidator(unittest.TestCase):
    #verifie si un mouv est acepte par le validateur
    def test_valid_move(self):
        board = ChessBoard()
        move_validator = MoveValidator(board)
        pawn = Pawn('white', board, (1, 0))
        
        self.assertTrue(move_validator.is_valid_move((1, 0), (1, 1)))

#verifie si un mouv est rejetee par le validateur
    def test_invalid_move(self):
        board = ChessBoard()
        move_validator = MoveValidator(board)
        pawn = Pawn('white', board, (1, 0)) 
        self.assertFalse(move_validator.is_valid_move((1, 0), (1, 2)))

    
