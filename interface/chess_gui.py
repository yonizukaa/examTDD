import tkinter as tk
from chess_game import ChessGame


class ChessGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Chess Game")
        self.game = ChessGame()
        
        # Création du tableau d'échecs graphique (Tkinter Canvas)
        self.chessboard_canvas = tk.Canvas(master, width=400, height=400, borderwidth=0, highlightthickness=0)
        self.chessboard_canvas.grid(row=0, column=0)
        self.draw_chessboard()

        # Bouton pour effectuer un mouvement (exemple)
        self.move_button = tk.Button(master, text="Effectuer un mouvement", command=self.make_move)
        self.move_button.grid(row=1, column=0)

    def draw_chessboard(self):
    # Efface le contenu précédent du canevas
        self.chessboard_canvas.delete("all")

    square_size = 50  # Taille d'une case du plateau

    for row in range(8):
        for col in range(8):
            x1, y1 = col * square_size, row * square_size
            x2, y2 = (col + 1) * square_size, (row + 1) * square_size

            # Dessine la case
            if (row + col) % 2 == 0:
                self.chessboard_canvas.create_rectangle(x1, y1, x2, y2, fill="white")
            else:
                self.chessboard_canvas.create_rectangle(x1, y1, x2, y2, fill="black")

            # Dessine la pièce s'il y en a une
            piece = self.game.board.get_piece_at_position((row, col))
            if piece:
                piece_symbol = piece.get_symbol()
                self.chessboard_canvas.create_text(x1 + square_size // 2, y1 + square_size // 2,
                                                   text=piece_symbol, font=("Arial", 16))

def make_move(self):
    # Exemple simplifié pour effectuer un mouvement depuis la console
    start = input("Entrez la position de départ (par exemple, 'e2'): ")
    end = input("Entrez la position d'arrivée (par exemple, 'e4'): ")

   
    if self.validate_input(start) and self.validate_input(end):
        start_position = self.convert_input_to_coordinates(start)
        end_position = self.convert_input_to_coordinates(end)

        
        self.game.make_move(start_position, end_position)
    else:
        print("Format de mouvement invalide. Utilisez le format 'ex', où e est la colonne (a-h) et x est la ligne (1-8).")

def validate_input(self, position):
    return len(position) == 2 and position[0].lower() in 'abcdefgh' and position[1] in '12345678'

def convert_input_to_coordinates(self, position):
    column = ord(position[0].lower()) - ord('a')
    row = int(position[1]) - 1
    return row, column
