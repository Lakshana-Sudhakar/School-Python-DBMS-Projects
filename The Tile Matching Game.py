import random
import tkinter as tk
from tkinter import messagebox

class TileMatchingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Tile Matching Game")
        self.root.resizable(False, False)

        # Game state variables
        self.attempts = 0
        self.matches_found = 0
        self.first_choice = None
        self.second_choice = None
        self.buttons = []
        
        # Board setup
        self.board = self.create_tiles()

        # Build GUI UI elements
        self.create_widgets()

    def create_tiles(self):
        """Generates 16 tiles (8 pairs) and shuffles them."""
        letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'] * 2
        random.shuffle(letters)
        return letters

    def create_widgets(self):
        """Creates the header label, 4x4 grid of buttons, and score counter."""
        # Header Label
        header = tk.Label(
            self.root, 
            text="Memory Tile Matching Game", 
            font=("Arial", 16, "bold"), 
            padx=10,
            pady=10
        )
        header.grid(row=0, column=0, columnspan=4)

        # 4x4 Button Grid
        for idx in range(16):
            btn = tk.Button(
                self.root,
                text="*",
                font=("Arial", 18, "bold"),
                width=5,
                height=2,
                command=lambda i=idx: self.on_tile_click(i)
            )
            row = (idx // 4) + 1
            col = idx % 4
            btn.grid(row=row, column=col, padx=5, pady=5)
            self.buttons.append(btn)

        # Attempt Counter Label
        self.attempts_label = tk.Label(
            self.root, 
            text="Attempts: 0", 
            font=("Arial", 12), 
            padx=10,
            pady=10
        )
        self.attempts_label.grid(row=5, column=0, columnspan=4)

    def on_tile_click(self, idx):
        """Handles user clicking on a tile."""
        # Prevent clicking an already revealed card or clicking while waiting for reset
        if self.buttons[idx]["text"] != "*" or self.second_choice is not None:
            return

        # Reveal the clicked tile
        self.buttons[idx].config(text=self.board[idx], state="disabled")

        if self.first_choice is None:
            # First tile picked
            self.first_choice = idx
        else:
            # Second tile picked
            self.second_choice = idx
            self.attempts += 1
            self.attempts_label.config(text=f"Attempts: {self.attempts}")
            self.check_match()

    def check_match(self):
        """Checks if the two revealed tiles match."""
        idx1 = self.first_choice
        idx2 = self.second_choice

        if self.board[idx1] == self.board[idx2]:
            # Match found
            self.matches_found += 1
            self.first_choice = None
            self.second_choice = None

            # Check for win condition (8 total pairs)
            if self.matches_found == 8:
                messagebox.showinfo(
                    "Congratulations!", 
                    f"You won in {self.attempts} attempts!"
                )
        else:
            # Not a match: flip back after a brief 800ms delay
            self.root.after(800, self.hide_tiles, idx1, idx2)

    def hide_tiles(self, idx1, idx2):
        """Flips unmatched tiles back over."""
        self.buttons[idx1].config(text="*", state="normal")
        self.buttons[idx2].config(text="*", state="normal")
        self.first_choice = None
        self.second_choice = None

# Run the Application
if __name__ == "__main__":
    root = tk.Tk()
    game = TileMatchingGame(root)
    root.mainloop()
