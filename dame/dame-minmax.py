import math


class Game:
    def __init__(self):
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
# hihihii
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

    def get_possible_moves(self):
        moves = []
        for i in range(6):
            for j in range(6):
                if self.board[i][j] == self.current_player:
                    if i - 1 >= 0 and j - 1 >= 0 and self.is_valid_move(i, j, i - 1, j - 1):
                        moves.append((i, j, i - 1, j - 1))
                    if i - 1 >= 0 and j + 1 <= 5 and self.is_valid_move(i, j, i - 1, j + 1):
                        moves.append((i, j, i - 1, j + 1))
                    if i + 1 <= 5 and j - 1 >= 0 and self.is_valid_move(i, j, i + 1, j - 1):
                        moves.append((i, j, i + 1, j - 1))
                    if i + 1 <= 5 and j + 1 <= 5 and self.is_valid_move(i, j, i + 1, j + 1):
                        moves.append((i, j, i + 1, j + 1))

                    if i - 2 >= 0 and j - 2 >= 0 and self.is_valid_jump(i, j, i - 2, j - 2):
                        moves.append((i, j, i - 2, j - 2))
                    if i - 2 >= 0 and j + 2 <= 5 and self.is_valid_jump(i, j, i - 2, j + 2):
                        moves.append((i, j, i - 2, j + 2))
                    if i + 2 <= 5 and j - 2 >= 0 and self.is_valid_jump(i, j, i + 2, j - 2):
                        moves.append((i, j, i + 2, j - 2))
                    if i + 2 <= 5 and j + 2 <= 5 and self.is_valid_jump(i, j, i + 2, j + 2):
                        moves.append((i, j, i + 2, j + 2))
        return moves

    def make_best_move(self):
        best_score = -math.inf
        best_move = None
        for move in self.get_possible_moves():
            temp_board = [row[:] for row in self.board]
            temp_current_player = self.current_player

            temp_game = Game()
            temp_game.board = temp_board
            temp_game.current_player = temp_current_player

            temp_game.make_move(move[0], move[1], move[2], move[3])
            score = temp_game.minimax(False)
            if score > best_score:
                best_score = score
                best_move = move

        self.make_move(best_move[0], best_move[1], best_move[2], best_move[3])

    def minimax(self, is_maximizing):
        if self.is_game_over():
            if self.current_player == 'X':
                return -1
            elif self.current_player == 'O':
                return 1

        if is_maximizing:
            best_score = -math.inf
            for move in self.get_possible_moves():
                temp_board = [row[:] for row in self.board]
                temp_current_player = self.current_player

                temp_game = Game()
                temp_game.board = temp_board
                temp_game.current_player = temp_current_player

                temp_game.make_move(move[0], move[1], move[2], move[3])
                score = temp_game.minimax(False)
                best_score = max(score, best_score)
            return best_score
        else:
            best_score = math.inf
            for move in self.get_possible_moves():
                temp_board = [row[:] for row in self.board]
                temp_current_player = self.current_player

                temp_game = Game()
                temp_game.board = temp_board
                temp_game.current_player = temp_current_player

                temp_game.make_move(move[0], move[1], move[2], move[3])
                score = temp_game.minimax(True)
                best_score = min(score, best_score)
            return best_score

    def play(self):
        while not self.game_over:
            self.print_board()
            print("It's", self.current_player, "player's turn.")

            if self.current_player == 'X':
                start_row = int(input("Enter the row of the piece you want to move: "))
                start_col = int(input("Enter the column of the piece you want to move: "))
                end_row = int(input("Enter the row where you want to move the piece: "))
                end_col = int(input("Enter the column where you want to move the piece: "))
                if self.make_move(start_row, start_col, end_row, end_col):
                    if self.is_game_over():
                        print("Congratulations! Player", self.current_player, "wins!")
                else:
                    print("Invalid move. Try again.")
            else:
                self.make_best_move()
                if self.is_game_over():
                    print("Sorry! Player", self.current_player, "wins!")


game = Game()
game.play()
