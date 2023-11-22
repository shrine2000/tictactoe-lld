class Board:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

    def display_board(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)

    def is_valid_move(self, row, col):
        return 0 <= row < 3 and 0 <= col < 3 and self.board[row][col] == ' '

    def place_marker(self, row, col, marker):
        self.board[row][col] = marker

    def is_winner(self, marker):
        for i in range(3):
            if all(self.board[i][j] == marker for j in range(3)) or \
               all(self.board[j][i] == marker for j in range(3)):
                return True
        return all(self.board[i][i] == marker for i in range(3)) or \
               all(self.board[i][2 - i] == marker for i in range(3))

    def is_full(self):
        return all(self.board[i][j] != ' ' for i in range(3) for j in range(3))
