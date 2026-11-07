def create_board():
    return [" "] * 9

def display_board(board):
    cells = [
        board[i] if board[i] != " " else str(i + 1)
        for i in range(9)
    ]
    print()
    print(f" {cells[0]} | {cells[1]} | {cells[2]} ")
    print("---+---+---")
    print(f" {cells[3]} | {cells[4]} | {cells[5]} ")
    print("---+---+---")
    print(f" {cells[6]} | {cells[7]} | {cells[8]} ")
    print()


def available_moves(board):
    return [i for i in range(9) if board[i] == " "]


def make_move(board, position, player):
    if position not in range(9):
        return False

    if board[position] != " ":
        return False

    board[position] = player
    return True


def check_winner(board):

    winning_combinations = [
        (0, 1, 2),  # First row
        (3, 4, 5),  # Second row
        (6, 7, 8),  # Third row
        (0, 3, 6),  # First column
        (1, 4, 7),  # Second column
        (2, 5, 8),  # Third column
        (0, 4, 8),  # Main diagonal
        (2, 4, 6)   # Other diagonal
    ]

    for a, b, c in winning_combinations:
        if board[a] == board[b] == board[c] != " ":
            return board[a]

    return None


def is_draw(board):
    return check_winner(board) is None and " " not in board


def game_over(board):
    return check_winner(board) is not None or is_draw(board)