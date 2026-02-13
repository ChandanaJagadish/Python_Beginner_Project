# Chess-game
♟️ Python Chessboard Simulator

A simple Python-based chessboard simulator built using dictionaries.
This project visually represents a chessboard in the console and allows flexible piece placement without enforcing chess rules.

📌 Features

Dictionary-based board representation (a1 to h8)

Two-character piece notation:

First letter → Color (w = white, b = black)

Second letter → Type (p, n, b, r, q, k)

Supports:

Standard starting position

Custom mid-game setups

Console-based board printing

Alternating square color simulation using text spacing

No external libraries required

🛠️ Technologies Used

Python 3

Dictionary data structure

Loops and string formatting

▶️ How It Works

The board is stored as a Python dictionary.

Keys represent board squares (a1 to h8).

Values store piece codes or None.

The board prints row-by-row from 8 to 1.

Columns print from a to h.

▶️ How to Run

Install Python (3.x recommended)

Clone the repository:

git clone https://github.com/your-username/python-chessboard.git

Run the file:

python chessboard.py

🎯 Example Piece Representation
Piece	Code
White Pawn	wp
Black Knight	bn
White Queen	wq
Black King	bk
⚠️ Limitations

Does NOT enforce chess rules

No move validation

Console-only interface

🚀 Future Improvements

Add move validation

Implement full chess rules

Add check/checkmate detection

Create GUI version (Tkinter or Pygame)
