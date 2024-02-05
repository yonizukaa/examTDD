from chess_board import ChessBoard


class ChessGame:
    def __init__(self):
        # Initialisation du jeu avec un plateau
        self.board = ChessBoard()
        

    def make_move(self, start, end):
        piece = self.board.get_piece_at_position(start)
        if piece is not None and piece.is_valid_move(end):
            self.board.move_piece(start, end)
            
        else:
            print("Mouvement invalide")

    def get_status(self):
        


        if __name__ == "__main__":
            game = ChessGame()
            game.board.print_board()

            game.make_move((1, 0), (2, 0))
            game.board.print_board()

            game.make_move((0, 1), (2, 0))  # Mouvement invalide