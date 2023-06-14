from guizero import info

from ui.board_game import BoardGame


class TicTacToe(BoardGame):

    def __init__(self, master, board_data=None, on_button_push=None):
        if board_data is None:
            board_data = [
                [' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ']
            ]
        super().__init__(master, board_data, on_button_push)

    def __push_button__(self, button, command, x, y, ai_move):
        # TODO: Verify if the move is legal
        # is_move_legal = command(x, y, ai_move)
        is_move_legal = True
        if is_move_legal:
            button.update_command(None)
            button.image = "assets/images/red.png"
        else:
            info(master=self.master, title="Invalid move", text="Das kannst du nicht machen!")

    def ai_move(self, x, y):
        button = self.__button_grid__[x][y]
        button.image = "assets/images/yellow.png"
        button.width = 50
        button.height = 50
        button.update_command(None)
