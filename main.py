#Project_2
"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Natallia Konanava
email: nataxa_87@seznam.cz
"""

print('''
Welcome to Tic Tac Toe
========================================
GAME RULES:
Each player can place one mark (or stone)
per turn on the 3x3 grid. The WINNER is
who succeeds in placing three of their
marks in a:
* horizontal,
* vertical or
* diagonal row
========================================
Let's start the game
----------------------------------------'''
)

def print_board(board):
    """zobrazí hrací plochu"""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board):
    """Kontroluje vítěze"""
    lines = board + list(map(list, zip(*board)))  # Řádky a sloupce
    diagonals = [[board[i][i] for i in range(3)], [board[i][2 - i] for i in range(3)]]
    lines.extend(diagonals)

    for line in lines:
        if line == ["X", "X", "X"]:
            return "X"
        elif line == ["O", "O", "O"]:
            return "O"
    return None


def is_draw(board):
    """Kontroluje remize"""
    return all(cell in ["X", "O"] for row in board for cell in row)


def get_move():
    """Pta u hrače číslo pole (1-9)."""
    while True:
        try:
            move = int(input("Please enter your move number: ")) - 1
            if move < 0 or move >= 9:
                raise ValueError
            return divmod(move, 3)  # Transformace na souřadnice (řádek, sloupec)
        except ValueError:
            print("Wrong enter. Please enter number from od 1 to 9.")


def tic_tac_toe():
    """Spustit hru."""
    board = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
    current_player = "X"

    while True:
        print_board(board)
        print(f"Player {current_player}")

        while True:
            row, col = get_move()
            if board[row][col] not in ["X", "O"]:
                board[row][col] = current_player
                break
            print("The field is occupied! Please try again.")

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Congratulations, the player {winner} WON!")
            break
        elif is_draw(board):
            print_board(board)
            print("Draw!")
            break

        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    tic_tac_toe()