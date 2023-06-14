import os

from guizero import Box, PushButton


def __customize_button__(widget):
    widget.tk.config(
        relief="flat",
        cursor="hand2")


class BoardGame:

    def __push_button__(self, button, command, x, y, ai_move):
        pass

    def ai_move(self, x, y):
        pass

    def __init__(self,
                 master,
                 board_data,
                 on_button_push=None,
                 ):
        """
            Creates BoardGame UI

            :param Container master:
                The Container (App, Box, etc.) the Game will belong to.

            :param List board_data:
                Initial state of the board.

            :param Callable on_button_push:
                A string containing the function to call on button click. Defaults to None
            """
        self.__button_grid__ = None
        self.master = master
        self.board_data = board_data
        self.on_button_push = on_button_push
        self.create_board()

    def __create_button__(self, master, y, x, cell):
        button_box = Box(master, height=50, width=50, grid=[y, x])
        button = PushButton(button_box, text=' ', height=50, width=50, pady=0, padx=0)
        button.update_command(self.__push_button__, [button, self.on_button_push, x, y, self.ai_move])
        __customize_button__(button)
        button.font = "Arial"
        button.text_size = "18"
        button.text_color = "blue"
        button.text = " "
        if cell == "X":
            button.image = os.path.abspath("ui/assets/images/red.png")
        elif cell == "O":
            button.image = os.path.abspath("ui/assets/images/yellow.png")

        if x % 2 == 0 and y % 2 == 0:
            button.bg = "grey"
        elif x % 2 == 1 and y % 2 == 1:
            button.bg = "grey"
        else:
            button.bg = "white"

        return button

    # Initialize Game UI and show initial state
    def create_board(self):

        box = Box(self.master, layout="grid", border=True)
        box.bg = "#000000"
        box.tk.config(borderwidth=2)
        buttons = []
        for x, row in enumerate(self.board_data):
            button_row = []
            for y, cell in enumerate(row):
                button = self.__create_button__(box, y, x, cell)
                button_row.append(button)
            buttons.append(button_row)

        self.__button_grid__ = buttons
