class Dame:
    """
     expected Array output to GUI:
        [
            [None, None, None, None, None, None],
            [None, None, None, None, None, None],
            [None, None, None, None, None, None],
            [None, None, None, None, None, None],
            [None, None, None, None, None, None],
            [None, None, None, None, None, None]
         ]
    """

    def __init__(self):
        self.board = [[' ' for _ in range(6)] for _ in range(6)]

        self.player1 = "Player 1"
        self.player2 = "Player 2"

        self.game_over = False

    def print_board(self):
        print('   1  2  3  4  5  6')
        for i in range(6):
            row = str(i) + '  '
            for j in range(6):
                row += self.board[i][j] + '  '
            print(row)

    def place_initial_pieces(self):
        for i in range(2):
            for j in range(6):
                if (i + j) % 2 == 0:
                    self.board[i][j] = 'X'
                    self.board[5 - i][j] = 'O'

    def main(self):
        self.place_initial_pieces()
        self.print_board()


game = Dame()
game.main()
