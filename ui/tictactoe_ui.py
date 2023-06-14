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
        if command(x, y, ai_move):
            button.update_command(None)
            button.image = "assets/images/red.png"

    def ai_move(self, x, y):
        button = self.__button_grid__[x][y]
        button.image = "assets/images/yellow.png"
        button.width = 50
        button.height = 50
        button.update_command(None)
