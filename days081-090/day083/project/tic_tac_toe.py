import random

EMPTY = '_'
CROSS = 'X️'
DOT = 'O'


class TicTacToe:
    POS_DICT = {
        1: (0, 0),
        2: (0, 1),
        3: (0, 2),
        4: (1, 0),
        5: (1, 1),
        6: (1, 2),
        7: (2, 0),
        8: (2, 1),
        9: (2, 2),
    }

    def __init__(self, players):
        self.board = [[EMPTY for _i in range(3)] for _j in range(3)]

        self.winners = {'DRAW': 0, players[0].upper(): 0, players[1].upper(): 0}
        self.player1 = random.choice(players)
        players.remove(self.player1)
        self.player2 = players[0]
        self.round = 1
        self.turn = 0
        self.game_over = False

    def start(self):
        print('\nRules:')
        print('  Player 1 always starts.')
        print('  Players are selected randomly for first round.')
        print('  Player 1 is "X", Player 2 is "O".')
        print('  You must select a number from 1 to 9')
        print('when choosing a move, as follows:')
        print('\n  1 2 3\n  4 5 6\n  7 8 9')
        print('\nFor this round:')
        print('Player 1:', self.player1)
        print('Player 2:', self.player2)

    def convert_pos(self, index):
        return self.POS_DICT.get(index, None)

    def is_available(self, row, col):
        return self.board[row][col] == EMPTY

    def play(self):
        index = int(input(f'Enter a position on the board {self.player1 if self.turn % 2 == 0 else self.player2}: '))
        pos = self.convert_pos(index)
        if pos is None:
            print('Invalid position entered!')
            return False
        row, col = pos
        if not self.is_available(row, col):
            print('Position is not a free space!')
            return False
        self.board[row][col] = CROSS if self.turn % 2 == 0 else DOT
        self.turn += 1
        return True

    def reset(self):
        if input('Type "yes" if you wish to keep playing? ').lower() == 'yes':
            self.board = [[EMPTY for _i in range(3)] for _j in range(3)]
            self.turn = 0
            self.round += 1
            self.player1, self.player2 = self.player2, self.player1
            print("\nATTENTION: The players have been switched!!!")
            print('\nFor this round:')
            print('Player 1:', self.player1)
            print('Player 2:', self.player2)
        else:
            self.game_over = True

    def final_output(self):
        print(f"\nYou have played {self.round} rounds.\n")
        for winner, score in self.winners.items():
            print(f'{winner} won {score} times.')
        del self.winners['DRAW']
        winner = max(self.winners, key=self.winners.get)
        print(f'\n{winner} is the final winner!')

    def check_board(self):
        b_dict = {
            1: self.board[0][0],
            2: self.board[0][1],
            3: self.board[0][2],
            4: self.board[1][0],
            5: self.board[1][1],
            6: self.board[1][2],
            7: self.board[2][0],
            8: self.board[2][1],
            9: self.board[2][2],
        }
        if b_dict[1] == b_dict[2] == b_dict[3] or b_dict[1] == b_dict[4] == b_dict[7]:
            return b_dict[1]
        if b_dict[4] == b_dict[5] == b_dict[6] or b_dict[2] == b_dict[5] == b_dict[8]:
            return b_dict[5]
        if b_dict[7] == b_dict[8] == b_dict[9] or b_dict[3] == b_dict[6] == b_dict[9]:
            return b_dict[9]
        if b_dict[1] == b_dict[5] == b_dict[9] or b_dict[3] == b_dict[5] == b_dict[7]:
            return b_dict[5]

    def check_game(self):
        if self.turn == 9:
            self.winners['DRAW'] += 1
            print("\nFinal board:")
            print(self)
            print("It's a DRAW!")
            self.reset()
        if self.turn >= 5:
            winner = self.check_board()
            if winner != EMPTY and winner is not None:
                print("\nFinal board:")
                print(self)
                winner_name = self.player1 if winner == CROSS else self.player2
                print(f'This round was won by {winner_name}!')
                self.winners[winner_name.upper()] += 1
                self.reset()

    def __str__(self):
        lines = [' '.join(self.board[x]) for x in range(3)]
        return '\n'.join(lines)


print("Welcome to Tic Tac Toe!")

game = TicTacToe(input('Enter the name for the players: ').split())
game.start()

while not game.game_over:
    print("\nCurrent board: ")
    print(game)
    if game.play():
        game.check_game()

game.final_output()
