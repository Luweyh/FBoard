# Author: Luwey Hon
# Date: 3/2/2020
# Description: This program creates a class name FBoard. Player x is
# trying to get their piece to corner square (7,7) and player o is trying
# to make it so player x doesn't have any legal moves.

class FBoard:
    """ This class represent an FBoard game"""

    def __init__(self):
        """ Initializes the board, games state, and x row and col"""
        self._board = [['' for _ in range(8)] for _ in range(8)]
        self._game_state = 'UNFINISHED'
        self._board[5][7] = 'o'
        self._board[6][6] = 'o'
        self._board[7][5] = 'o'
        self._board[7][7] = 'o'
        self._board[0][0] = 'x'
        self.x_row = 0
        self.x_col = 0



    def get_game_state(self):
        """ returns the current game state"""
        return self._game_state

    def test_o_win(self):
        """ Test to see if o wins"""

        row = self.x_row
        col = self.x_col

        # Position 1
        row_pos_1 = row - 1
        col_pos_1 = col - 1
        if 0 <= row_pos_1 <= 7 and 0 <= col_pos_1 <= 7:      # test if it's in bounds
            if self._board[row_pos_1][col_pos_1] == '':     # see if it's empty
                return False

        # Position 2
        row_pos_2 = row - 1
        col_pos_2 = col + 1
        if 0 <= row_pos_2 <= 7 and 0 <= col_pos_2 <= 7:      # test if it's in bounds
            if self._board[row_pos_2][col_pos_2] == '':     # see if it's empty
                return False

        # Position 3
        row_pos_3 = row + 1
        col_pos_3 = col - 1
        if 0 <= row_pos_3 <= 7 and 0 <= col_pos_3 <= 7:      # test if it's in bounds
            if self._board[row_pos_3][col_pos_3] == '':     # test if it's empty
                return False

        # Position 4
        row_pos_4 = row + 1
        col_pos_4 = col + 1
        if 0 <= row_pos_4 <= 7 and 0 <= col_pos_4 <= 7:      # test if it's in bounds
            if self._board[row_pos_4][col_pos_4] == '':     # test if it's empty
                return False

        # if the all the conditions passes, the test_o_win returns true
        return True

    def move_x(self, row, col):
        """ This function moves x """

        # checks to see if it finished
        if self._game_state != 'UNFINISHED':
            return False

        # makes sure the move is inbound
        if (not(row >= 0 and row < 8)) or (not(col >=0 and col < 8)):
            return False

        # check to see if it the space is empty
        if self._board[row][col] != '':
            return False

        # checking if move is eligible. x can't move directly above or below
        if (self.x_row - 1 == row and self.x_col == col) or (self.x_row + 1 == row and self.x_col == col):
            return False

        # checking if move is eligible. x can't move directly to its left or right
        if (self.x_col - 1 == col and self.x_row == row) or (self.x_col + 1 == col and self.x_row == row):
            return False

        # check to see if it moves then more than one space
        if abs(self.x_row - row) > 1 or abs(self.x_col - col) > 1:
            return False


        # Updates the board and moves x to the new spot
        self._board[row][col] = 'x'
        self._board[self.x_row][self.x_col] = ''
        self.x_row = row
        self.x_col = col

        # if x wins
        if self._board[7][7] == 'x':
            self._game_state = 'X_WON'
            return True

        return True

    def move_o(self, from_row, from_col, to_row, to_col):
        """ This functions moves the o character"""

        # Make sures the game is not finished
        if self._game_state != 'UNFINISHED':
            return False

        # checking if the pieces are in bounds
        if (to_row < 0 or to_row >= 8) or (to_col < 0 or to_col >= 8):
            return False

        # check if the spot is empty
        if self._board[to_row][to_col] != '':
            return False

        # o can't move directly to its left or right
        if (from_row == to_row and from_col - 1 == to_col) or (from_row == to_row and from_col + 1 == to_col):
            return False

        # o can't move directly above or below
        if (from_col == to_col and from_row - 1 == to_row) or (from_col == to_col and from_row + 1 == to_row):
            return False

        # o can't move diagonly to the right down (row and column both cannot increase)
        if from_row + 1 == to_row and from_col + 1 == to_col:
            return False

        if abs(from_row - to_row) > 1 or abs(from_col - to_col) > 1:
            return False


        # Updates the board and moves 'o'
        self._board[to_row][to_col] = 'o'
        self._board[from_row][from_col] = ''

        # checks if o wins
        if self.test_o_win():
            self._game_state = "O_WON"    # change game state to O_WON if the conditions in self.test_o_wins() are met
            return True

        return True


# The code below is for some debugging purposes (it prints the board and test)

#
#     def print_board(self):
#         """ Prints the board"""
#         count = 0
#         for row in self._board:
#             print(str(count) + " " + str(row))
#             count += 1
#
# 
# if __name__ == '__main__':
#     fb = FBoard()
#
#     while fb.get_game_state() == 'UNFINISHED':
#         fb.print_board()
#         player = input("which player?")
#         if player == 'x':
#             row = input("which row to move x?")
#             col = input("which column to move x?")
#             fb.move_x(int(row), int(col))
#
#
#         if player == 'o':
#             from_row = input("from which row in o?")
#             from_col = input("from which col in o?")
#             row = input("to what row for o?")
#             col = input('to what column for o?')
#             print("You have inserted o to move from ({}, {}) to ({}, {})".format(from_row, from_col, row, col))
#             fb.move_o(int(from_row), int(from_col), int(row), int(col))










