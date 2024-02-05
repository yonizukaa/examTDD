class ChessBoard:
    def __init__(self):
        # Initialisation du plateau de jeu
        self.board = [[None] * 8 for _ in range(8)]

    def place_piece(self, piece, position):
        x, y = position
        self.board[x][y] = piece

    def move_piece(self, start, end):
        x_start, y_start = start
        x_end, y_end = end
        piece = self.board[x_start][y_start]
        self.board[x_end][y_end] = piece
        self.board[x_start][y_start] = None

    def get_piece_at_position(self, position):
        x, y = position
        return self.board[x][y]

    def print_board(self):
        for row in self.board:
            print(row)