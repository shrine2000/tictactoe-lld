from models.board import Board
from models.player import Player

class TicTacToe:
    def __init__(self):
        self.game_board = Board() 
        self.current_player = None
        self.players = []

    def setup_game(self):
        player1_name = input("Enter Player 1's name: ")
        player2_name = input("Enter Player 2's name: ")
        self.players.append(Player(player1_name, 'X'))  
        self.players.append(Player(player2_name, 'O'))
        self.current_player = self.players[0]

    def switch_player(self):
        if self.current_player == self.players[0]:
            self.current_player = self.players[1]
        else:
            self.current_player = self.players[0]

    def play_game(self):
        self.setup_game()
        while not self.game_board.is_full():
            self.game_board.display_board()
            print(f"{self.current_player.name}'s turn ({self.current_player.marker})")
            row, col = self.current_player.make_move()
            if self.game_board.is_valid_move(row, col):
                self.game_board.place_marker(row, col, self.current_player.marker)
                if self.game_board.is_winner(self.current_player.marker):
                    print(f"{self.current_player.name} wins!")
                    break
                elif self.game_board.is_full():
                    print("It's a draw!")
                    break
                self.switch_player()
            else:
                print("Invalid move. Try again.")
        print("Game Over!")
