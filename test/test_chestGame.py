import unittest
from chess_game import ChessGame
from gameplay.game_status import GameStatus


class TestChessGame(unittest.TestCase):
    def test_initial_game_state(self):
        game = ChessGame()
        self.assertEqual(game.get_status(), GameStatus.IN_PROGRESS)
        
# Effectuez un mouvement valide et vérifiez que le statut du jeu est toujours en cours
    def test_valid_move(self):
        game = ChessGame()
        
        game.make_move('e2', 'e4')
        self.assertEqual(game.get_status(), GameStatus.IN_PROGRESS)

# Effectue un mouvement invalide et vérifie que le statut du jeu est échec (ou autre statut approprié)
    def test_invalid_move(self):
        game = ChessGame()
        
        game.make_move('e2', 'e5')
        self.assertEqual(game.get_status(), GameStatus.CHECK)

# Teste un scénario d'échec et mat
    def test_checkmate(self):
    
        game = ChessGame()

        game.make_move('e2', 'e4')  # Premier coup, avance le pion du roi blanc
        game.make_move('e7', 'e5')  # Premier coup, avance le pion du roi noir
        game.make_move('d2', 'd4')  # Deuxième coup, avance le pion de la dame blanc
        game.make_move('e5', 'd4')  # Deuxième coup, capture du pion par le pion noir
        game.make_move('d1', 'h5')  # Troisième coup, déplacement de la dame blanc
        game.make_move('g8', 'f6')  # Troisième coup, déplacement du cavalier noir
        game.make_move('h5', 'f7')  # Quatrième coup, déplacement de la dame blanc
        game.make_move('f8', 'e7')  # Quatrième coup, déplacement du roi noir

        # le roi noir est en échec et mat
        self.assertEqual(game.get_status(), GameStatus.CHECKMATE)
