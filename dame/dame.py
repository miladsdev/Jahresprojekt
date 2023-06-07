class Game:
    def __init__(self):
        #self.board = [[' ' for _ in range(6)] for _ in range(6)]

        # Test: if reaching other side winns
        self.board = [
            ['X', ' ', 'X', ' ', 'X', ' '],
            [' ', 'X', ' ', 'X', ' ', 'X'],
            [' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' '],
            [' ', 'O', ' ', 'O', ' ', 'O'],
            ['O', ' ', 'O', ' ', 'O', ' ']
        ]

        self.current_player = 'X'
        self.game_over = False

    def print_board(self):
        print('   0  1  2  3  4  5')
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

    def is_valid_move(self, start_row, start_col, end_row, end_col):
        if self.board[start_row][start_col] != self.current_player:
            return False
        if self.board[end_row][end_col] != ' ':
            return False
        if abs(start_row - end_row) != 1 or abs(start_col - end_col) != 1:
            return False
        return True

    def is_valid_jump(self, start_row, start_col, end_row, end_col):
        if self.board[start_row][start_col] != self.current_player:
            return False
        if self.board[end_row][end_col] != ' ':
            return False
        if abs(start_row - end_row) != 2 or abs(start_col - end_col) != 2:
            return False
        mid_row = (start_row + end_row) // 2
        mid_col = (start_col + end_col) // 2
        if self.board[mid_row][mid_col] == ' ':
            return False
        if self.board[mid_row][mid_col] == self.current_player:
            return False
        return True

    def make_move(self, start_row, start_col, end_row, end_col):
        if self.is_valid_move(start_row, start_col, end_row, end_col):
            self.board[end_row][end_col] = self.board[start_row][start_col]
            self.board[start_row][start_col] = ' '
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            return True
        elif self.is_valid_jump(start_row, start_col, end_row, end_col):
            mid_row = (start_row + end_row) // 2
            mid_col = (start_col + end_col) // 2
            self.board[end_row][end_col] = self.board[start_row][start_col]
            self.board[start_row][start_col] = ' '
            self.board[mid_row][mid_col] = ' '
            if not self.has_valid_jump(end_row, end_col):
                self.current_player = 'O' if self.current_player == 'X' else 'X'
            return True
        else:
            return False

    def has_valid_move(self, row, col):
        if self.is_valid_move(row, col, row - 1, col - 1):
            return True
        if self.is_valid_move(row, col, row - 1, col + 1):
            return True
        if self.is_valid_move(row, col, row + 1, col - 1):
            return True
        if self.is_valid_move(row, col, row + 1, col + 1):
            return True
        return False

    def has_valid_jump(self, row, col):
        if self.is_valid_jump(row, col, row - 2, col - 2):
            return True
        if self.is_valid_jump(row, col, row - 2, col + 2):
            return True
        if self.is_valid_jump(row, col, row + 2, col - 2):
            return True
        if self.is_valid_jump(row, col, row + 2, col + 2):
            return True
        return False

    def is_game_over(self):
        if self.player_reached_other_side():
            self.game_over = True
            return True

        for i in range(6):
            for j in range(6):
                if self.board[i][j] == self.current_player and (self.has_valid_move(i, j) or self.has_valid_jump(i, j)):
                    return False
        self.game_over = True
        return True

    def player_reached_other_side(self):
        if 'O' in self.board[0]:
            self.current_player = 'O'
            return True
        elif 'X' in self.board[5]:
            self.current_player = 'X'
            return True

        return False

    def play(self):
        self.place_initial_pieces()
        while not self.game_over:
            self.print_board()
            print("It's", self.current_player, "player's turn.")
            start_row = int(input("Enter the row of the piece you want to move: "))
            start_col = int(input("Enter the column of the piece you want to move: "))
            end_row = int(input("Enter the row where you want to move the piece: "))
            end_col = int(input("Enter the column where you want to move the piece: "))
            if self.make_move(start_row, start_col, end_row, end_col):
                if self.is_game_over():
                    print("Congratulations! Player", self.current_player, "wins!")
            else:
                print("Invalid move. Try again.")

game = Game()
game.play()
