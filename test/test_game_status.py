import unittest

from chess_game import ChessGame
from gameplay.game_status import GameStatus


class TestChessGameStatus(unittest.TestCase):
    def test_game_in_progress(self):
        game = ChessGame()
        self.assertEqual(game.get_status(), GameStatus.IN_PROGRESS)

    def test_check(self):
        game = ChessGame()
        game.make_move('e2', 'e4')  # Un mouvement pour créer une situation d'échec
        game.make_move('e7', 'e5')  # Un mouvement pour répondre
        game.make_move('d2', 'd4')  # Un autre mouvement
        game.make_move('e5', 'd4')  # Capture pour mettre le roi noir en échec

        self.assertEqual(game.get_status(), GameStatus.CHECK)

    def test_checkmate(self):
        game = ChessGame()
        # Création d'une situation d'échec et mat 
        game.make_move('e2', 'e4')
        game.make_move('f7', 'f6')
        game.make_move('d1', 'h5')
        game.make_move('g8', 'f6')
        game.make_move('h5', 'f7')

        self.assertEqual(game.get_status(), GameStatus.CHECKMATE)

    def test_stalemate(self):
        game = ChessGame()
        # Création d'une situation de pat 
        game.make_move('e2', 'e4')
        game.make_move('f7', 'f5')
        game.make_move('d2', 'd4')
        game.make_move('e8', 'f7')
        game.make_move('d4', 'e5')
        game.make_move('f7', 'e8')
        game.make_move('e5', 'f6')
        game.make_move('e8', 'f7')
        game.make_move('f6', 'g7')
        game.make_move('f7', 'g8')
        game.make_move('g7', 'h8')

        self.assertEqual(game.get_status(), GameStatus.STALEMATE)

    def test_draw(self):
        game = ChessGame()
        # Création d'une situation de partie nulle 
        game.make_move('e2', 'e4')
        game.make_move('e7', 'e5')
        game.make_move('g1', 'f3')
        game.make_move('b8', 'c6')
        game.make_move('f1', 'c4')
        game.make_move('g8', 'f6')
        game.make_move('e1', 'g1')
        game.make_move('f8', 'e7')
        game.make_move('c1', 'e3')
        game.make_move('e8', 'g8')
        game.make_move('e3', 'd4')
        game.make_move('g8', 'h8')
        game.make_move('d4', 'c5')
        game.make_move('h8', 'g8')
        game.make_move('c5', 'd6')
        game.make_move('g8', 'h8')
        game.make_move('d6', 'e7')
        game.make_move('h8', 'g8')
        game.make_move('e7', 'f8')

        self.assertEqual(game.get_status(), GameStatus.DRAW)

if __name__ == "__main__":
    unittest.main()
