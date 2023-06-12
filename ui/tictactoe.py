from guizero import Box, PushButton


def __push_button__(button, command, x, y):
    button.update_command(None)
    command(button, x, y)


def __customize_button__(widget):
    widget.tk.config(
        relief="flat",
        cursor="hand2")


class TicTacToe:

    def __init__(self,
                 master,
                 board_data=None,
                 on_button_push=None,
                 ):
        """
            Creates TicTacToe UI

            :param Container master:
                The Container (App, Box, etc.) the Game will belong to.

            :param List board_data:
                Initial state of the board. Defaults to empty 6x6 Array.

            :param Callable on_button_push:
                A string containing the function to call on button click. Defaults to None
            """
        if board_data is None:
            board_data = [
                [' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ']
            ]
        self.master = master
        self.board_data = board_data
        self.on_button_push = on_button_push
        self.create_board()

    # Initialize Game UI and show initial state
    def create_board(self):
        box = Box(self.master, layout="grid", border=True)
        box.bg = "#000000"
        box.tk.config(borderwidth=2)
        buttons = []
        for x, row in enumerate(self.board_data):
            button_row = []
            for y, cell in enumerate(row):
                button_box = Box(box, height=50, width=50, grid=[y, x])
                button = PushButton(button_box, text=' ', height=50, width=50, pady=0, padx=0)
                button.update_command(__push_button__, [button, self.on_button_push, x, y])
                button.font = "Arial"
                button.text_size = "18"
                button.text_color = "blue"
                if cell == "X":
                    button.update_command(None)
                    button.image = "assets/images/red.png"
                elif cell == "O":
                    button.update_command(None)
                    button.image = "assets/images/yellow.png"
                else:
                    button.text = " "

                if x % 2 == 0 and y % 2 == 0:
                    button.bg = "white"
                elif x % 2 == 1 and y % 2 == 1:
                    button.bg = "white"
                else:
                    button.bg = "grey"
                __customize_button__(button)

                button_row.append(button)
            buttons.append(button_row)
