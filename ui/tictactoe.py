from guizero import Box, PushButton


def __push_button__(button, command, x, y):
    button.update_command(None)
    command(button, x, y)


class TicTacToe:

    def __init__(self, master, board_data, on_button_push):
        """
            Creates TicTacToe UI

            :param Container master:
                The Container (App, Box, etc.) the Game will belong to.

            :param List board_data:
                Initial state of the board.

            :param Callable on_button_push:
                A string containing the function to call on button click.
            """
        self.master = master
        self.board_data = board_data
        self.on_button_push = on_button_push
        self.create_board()
        self.pushed_button = None

    # Initialize Game UI and show initial state
    def create_board(self):
        box = Box(self.master, layout="grid", border=True)
        buttons = []
        for x, row in enumerate(self.board_data):
            button_row = []
            for y, cell in enumerate(row):
                button = PushButton(box, text=' ', grid=[y, x], width=2, pady=0, padx=0)
                button.update_command(__push_button__, [button, self.on_button_push, x, y])
                # button.args = (x, y)
                button.font = "Arial"
                button.text_size = "18"
                button.text_color = "blue"
                if cell != " ":
                    button.text = cell
                    button.update_command(None)
                else:
                    button.text = " "

                if x % 2 == 0 and y % 2 == 0:
                    button.bg = "white"
                elif x % 2 == 1 and y % 2 == 1:
                    button.bg = "white"
                else:
                    button.bg = "grey"
                button_row.append(button)
            buttons.append(button_row)
