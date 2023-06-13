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

    def __push_button__(self, button, command, x, y):
        button.update_command(None)
        command(button, x, y)
