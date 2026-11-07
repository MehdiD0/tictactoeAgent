from game import check_winner, available_moves


def evaluate(board):
    winner = check_winner(board)

    if winner == "O":
        return 10
    elif winner == "X":
        return -10
    else:
        return 0


def minimax(board, is_maximizing, depth=0):
    winner = check_winner(board)

    if winner == "O":
        return 10 - depth
    if winner == "X":
        return depth - 10
    moves = available_moves(board)
    if len(moves) == 0:
        return 0

    if is_maximizing:
        best_score = float("-inf")

        for move in moves:
            board[move] = "O"
            score = minimax(board, False, depth + 1)
            board[move] = " "
            best_score = max(best_score, score)
        return best_score

    else:
        best_score = float("inf")

        for move in moves:
            board[move] = "X"
            score = minimax(board, True, depth + 1)
            board[move] = " "
            best_score = min(best_score, score)
        return best_score


def get_best_move(board):
    best_score = float("-inf")
    best_move = None

    for move in available_moves(board):
        board[move] = "O"
        score = minimax(board, False, 1)
        board[move] = " "
        if score > best_score:
            best_score = score
            best_move = move

    return best_move                