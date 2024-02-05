import unittest

from chess_game import ChessGame


class TestInitialPlacement(unittest.TestCase):
    def test_initial_piece_placement(self):
        game = ChessGame()

        # Vérifie les positions initiales des pièces blanches
        self.assertEqual(game.get_piece_at('a1'), 'WR')  # Tour blanche
        self.assertEqual(game.get_piece_at('b1'), 'WN')  # Cavalier blanc
        self.assertEqual(game.get_piece_at('c1'), 'WB')  # Fou blanc
        self.assertEqual(game.get_piece_at('d1'), 'WQ')  # Reine blanche
        self.assertEqual(game.get_piece_at('e1'), 'WK')  # Roi blanc
        self.assertEqual(game.get_piece_at('f1'), 'WB')  # Fou blanc
        self.assertEqual(game.get_piece_at('g1'), 'WN')  # Cavalier blanc
        self.assertEqual(game.get_piece_at('h1'), 'WR')  # Tour blanche

        # Vérifie les positions initiales des pions blancs
        for col in 'abcdefgh':
            self.assertEqual(game.get_piece_at(col + '2'), 'WP')  # Pion blanc

        # Vérifie les positions initiales des pièces noires
        self.assertEqual(game.get_piece_at('a8'), 'BR')  # Tour noire
        self.assertEqual(game.get_piece_at('b8'), 'BN')  # Cavalier noir
        self.assertEqual(game.get_piece_at('c8'), 'BB')  # Fou noir
        self.assertEqual(game.get_piece_at('d8'), 'BQ')  # Reine noire
        self.assertEqual(game.get_piece_at('e8'), 'BK')  # Roi noir
        self.assertEqual(game.get_piece_at('f8'), 'BB')  # Fou noir
        self.assertEqual(game.get_piece_at('g8'), 'BN')  # Cavalier noir
        self.assertEqual(game.get_piece_at('h8'), 'BR')  # Tour noire

        # Vérifie les positions initiales des pions noirs
        for col in 'abcdefgh':
            self.assertEqual(game.get_piece_at(col + '7'), 'BP')  # Pion noir

if __name__ == "__main__":
    unittest.main()
