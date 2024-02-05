import unittest
from chess_game import ChessGame


class TestPieceCaptures(unittest.TestCase):
    def test_pawn_capture(self):
        game = ChessGame()
        # Place un pion blanc et un pion noir pour la capture
        game.place_piece('e4', 'WP')
        game.place_piece('d5', 'BP')

        # Effectue une capture avec un pion blanc
        game.make_move('e4', 'd5')
        self.assertIsNone(game.get_piece_at('e4'))  # Vérifie que le pion blanc a été capturé
        self.assertEqual(game.get_piece_at('d5'), 'WP')  # Vérifie que le pion noir est toujours en place

    def test_knight_capture(self):
        game = ChessGame()
        # Place un cavalier blanc et un pion noir pour la capture
        game.place_piece('g5', 'WN')
        game.place_piece('f7', 'BP')

        # Effectue une capture avec un cavalier blanc
        game.make_move('g5', 'f7')
        self.assertIsNone(game.get_piece_at('g5'))  # Vérifie que le cavalier blanc a été capturé
        self.assertEqual(game.get_piece_at('f7'), 'WN')  # Vérifie que le pion noir est toujours en place

    def test_bishop_capture(self):
        game = ChessGame()
        # Place un fou blanc et un pion noir pour la capture
        game.place_piece('c4', 'WB')
        game.place_piece('d5', 'BP')

        # Effectue une capture avec un fou blanc
        game.make_move('c4', 'd5')
        self.assertIsNone(game.get_piece_at('c4'))  # Vérifie que le fou blanc a été capturé
        self.assertEqual(game.get_piece_at('d5'), 'WB')  # Vérifie que le pion noir est toujours en place

    def test_rook_capture(self):
        game = ChessGame()
        # Place une tour blanche et un pion noir pour la capture
        game.place_piece('a3', 'WR')
        game.place_piece('a7', 'BP')

        # Effectue une capture avec une tour blanche
        game.make_move('a3', 'a7')
        self.assertIsNone(game.get_piece_at('a3'))  # Vérifie que la tour blanche a été capturée
        self.assertEqual(game.get_piece_at('a7'), 'WR')  # Vérifie que le pion noir est toujours en place

    def test_queen_capture(self):
        game = ChessGame()
        # Place une reine blanche et un pion noir pour la capture
        game.place_piece('d4', 'WQ')
        game.place_piece('f6', 'BP')

        # Effectue une capture avec une reine blanche
        game.make_move('d4', 'f6')
        self.assertIsNone(game.get_piece_at('d4'))  # Vérifie que la reine blanche a été capturée
        self.assertEqual(game.get_piece_at('f6'), 'WQ')  # Vérifie que le pion noir est toujours en place

    def test_king_capture(self):
        game = ChessGame()
        # Place  un roi blanc et un pion noir pour la capture
        game.place_piece('e1', 'WK')
        game.place_piece('f7', 'BP')

        # Effectue une capture avec un roi blanc
        game.make_move('e1', 'f7')
        self.assertIsNone(game.get_piece_at('e1'))  # Vérifie que le roi blanc a été capturé
        self.assertEqual(game.get_piece_at('f7'), 'WK')  # Vérifie que le pion noir est toujours en place

if __name__ == "__main__":
    unittest.main()
