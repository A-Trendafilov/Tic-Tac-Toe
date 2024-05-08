import os
import random

import numpy as np


class TicTacToe:
    def __init__(self):
        self.board = np.full((3, 3), " ")
        self.player_symbol = "X"
        self.computer_symbol = "O"

    def print_board(self):
        print("  1   2   3")
        for i in range(3):
            print(f"{i * 3 + 1} {' | '.join(self.board[i])}")
            if i < 2:
                print(" ---|---|---")

    @staticmethod
    def clear_screen():
        # Clear the screen based on the operating system
        os.system("cls" if os.name == "nt" else "clear")

    @staticmethod
    def convert_input_to_index(position):
        # Convert player input (1-9) to row and column indices
        position -= 1
        row = position // 3
        col = position % 3
        return row, col

    def check_winner(self, player):
        # Check rows, columns, and diagonals for a winner
        player_check = np.full(3, player)
        for i in range(3):
            if np.array_equal(self.board[i], player_check):
                return player
            if np.array_equal(self.board[:, i], player_check):
                return player
        if np.array_equal(np.diag(self.board), player_check) or np.array_equal(
                np.diag(np.fliplr(self.board)), player_check
        ):
            return player
        return None

    def player_move(self):
        while True:
            try:
                position = input("Enter your move (1-9 to play, 0 to exit): ")
                if position == "0":
                    print("Exiting the game...")
                    exit()  # Exit the game if the player enters '0'
                position = int(position)
                if position < 1 or position > 9:
                    print("Invalid input. Please enter a number between 1 and 9.")
                    continue
                row, col = self.convert_input_to_index(position)

                if self.board[row][col] == " ":
                    self.board[row][col] = self.player_symbol
                    break
                else:
                    print("That position is already taken. Try again.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 9.")

    def computer_move(self):
        # Check for winning moves
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == " ":
                    self.board[i][j] = self.computer_symbol
                    if self.check_winner(self.computer_symbol):
                        return
                    else:
                        self.board[i][j] = " "

        # Check for blocking moves
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == " ":
                    self.board[i][j] = self.player_symbol
                    if self.check_winner(self.player_symbol):
                        self.board[i][j] = self.computer_symbol
                        return
                    else:
                        self.board[i][j] = " "

        # If no winning or blocking moves, make a random move
        empty_cells = [
            (i, j) for i in range(3) for j in range(3) if self.board[i][j] == " "
        ]
        if empty_cells:
            random_row, random_col = random.choice(empty_cells)
            self.board[random_row][random_col] = self.computer_symbol
