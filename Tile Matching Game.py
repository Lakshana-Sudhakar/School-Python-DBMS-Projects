## HANDWRITTEN CODE

##import random
##
##def create_tiles():
##    tiles = [('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'),
##             ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H')] * 2
##    random.shuffle(tiles)
##    d={}
##    for i in range(16):
##        d[i]=tiles[i]
##    return d
##
##def display_board(b,r):
##    for i in range(4):
##        for j in range(4):
##            idx=i*4+j
##            if idx in r:
##                print(b[idx][0], end=" ")
##            else:
##                print("*",end=" ")
##        print()
##
##def tile_matching_game():
##    b=create_tiles()
##    r=[]
##    attempts=0
##    while len(r) < len(b):
##        display_board(b,r)
##        print("Select tiles(1-16)")
##        while True:
##            c1=input("enter a tile no b/w 1 to 16")
##            if c1.isdigit():
##                c1=int(c1)-1
##                if 0<= c1 <16:
##                    break
##                else:
##                    print("invalid input, enter a no between 1 and 16")
##            else:
##                print("invalid input. enter a number")
##
##        while True:
##            c2=input("enter a tile no b/w 1 to 16")
##            if c2.isdigit():
##                c2=int(c2)-1
##                if 0<= c2 <16 and c1!=c2:
##                    break
##                elif c1==c2:
##                    print("u can't pick the same tile twice")
##                else:
##                    print("invalid input, enter a no between 1 and 16")
##            else:
##                print("invalid input. enter a number")
##
##        if b[c1]==b[c2]:
##            if b[c1] not in r:
##                r.append(c1)
##            if b[c2] not in r:
##                r.append(c2)
##            print("it's a match")
##        else:
##            print("try again, not a match")
##
##        attempts=attempts+1
##
##    display_board(b,r)
##    print("you won in "+ str(attempts) +" attempts!")
##
##tile_matching_game()

## GUI ADDED CODE

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
