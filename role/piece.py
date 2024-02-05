class Piece:
    def __init__(self, color, board, position):
        self.color = color
        self.board = board
        self.position = position

    def get_valid_moves(self):
        raise NotImplementedError("La méthode get_valid_moves doit être implémentée dans les sous-classes.")

    def move(self, end_position):
        raise NotImplementedError("La méthode move doit être implémentée dans les sous-classes.")

    def is_valid_move(self, end_position):
        valid_moves = self.get_valid_moves()
        return end_position in valid_moves