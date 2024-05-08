from utility import TicTacToe


def main():
    game = TicTacToe()
    print("Welcome to Tic Tac Toe!")

    while True:
        game.clear_screen()
        game.print_board()

        # Player's move
        game.player_move()
        game.clear_screen()
        game.print_board()
        if game.check_winner(game.player_symbol):
            print("Congratulations! You win!")
            break
        elif " " not in game.board:
            print("It's a tie!")
            break

        # Computer's move
        game.computer_move()
        game.clear_screen()
        game.print_board()
        if game.check_winner(game.computer_symbol):
            print("Computer wins!")
            break
        elif " " not in game.board:
            print("It's a tie!")
            break


if __name__ == "__main__":
    main()
