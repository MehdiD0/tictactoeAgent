from game import *

from ai import get_best_move


def play_game():

    board = create_board()

    print("\n================================")
    print("       XO AI - TIC TAC TOE")
    print("================================")
    print("You are X | AI is O")
    print("Choose a position from 1 to 9.")

    display_board(board)

    while not game_over(board):
    
    # ----------------------------------------- 

        # HUMAN TURN

        while True:

            try:
                position = int(input("Your move (1-9): ")) - 1

                if make_move(board, position, "X"):
                    break

                print("Invalid position! Choose an empty cell.")

            except ValueError:
                print("Please enter a valid number.")

        display_board(board)

        if check_winner(board) == "X":
            print("Congratulations! You won!")
            break

        if is_draw(board):
            print("It's a draw!")
            break

    # -----------------------------------------    

        # AI TURN

        ai_move = get_best_move(board)

        make_move(board, ai_move, "O")

        print(f"AI played position {ai_move + 1}")

        # Display board after AI move
        display_board(board)

        # Check if AI won
        if check_winner(board) == "O":
            print("AI wins! Better luck next time.")
            break

        if is_draw(board):
            print("It's a draw!")
            break


def main():

    while True:

        play_game()

        print("\n================================")
        answer = input("Play again? (y/n): ").strip().lower()

        if answer != "y":
            print("Thanks for playing XO AI!")
            break


if __name__ == "__main__":
    main()