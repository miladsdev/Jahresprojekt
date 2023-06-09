from guizero import PushButton, Box, App

from ui.highscore import Highscore
from ui.tictactoe import TicTacToe


def __create_help_button__(master):
    help_button = PushButton(master, text="?", align="right")
    help_button.tk.config(width=5,
                          height=1,
                          borderwidth=0,
                          relief="raised",
                          activeforeground='darkgray',
                          activebackground='green',
                          highlightthickness=0,
                          # highlightcolor="blue",
                          bg='blue',
                          fg='orange',
                          cursor="hand2"
                          )
    return help_button


class GameWindow:

    def __init__(self,
                 game_mode,
                 initial_state=None,
                 command_button_pushed=None,
                 highscore_list=None):
        """
                    Creates TicTacToe UI
                    :param game_mode
                        String game_mode. ['tictactoe', 'dame']

                    :param List initial_state:
                        Initial state of the board. Defaults to empty 6x6 Array (tictactoe) or initial state of dame.

                    :param Callable command_button_pushed:
                        A string containing the function to call on button click. Defaults to None

                    :param List highscore_list:
                        List of the highscore String names to display. [0] = 1st place, (max) [9] = 10th place
                    """
        self.__window_title__ = None
        self.__game_mode__ = game_mode
        self.__initial_state__ = initial_state
        self.__command_button_pushed__ = command_button_pushed
        self.__highscore_list__ = highscore_list

    def __set_initial_state__(self):
        if self.__initial_state__ is not None:
            return
        if self.__game_mode__ == "dame":
            self.__initial_state__ = [
                ['X', ' ', 'X', ' ', 'X', ' '],
                [' ', 'X', ' ', 'X', ' ', 'X'],
                [' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' '],
                [' ', 'O', ' ', 'O', ' ', 'O'],
                ['O', ' ', 'O', ' ', 'O', ' ']
            ]
        elif self.__game_mode__ == "tictactoe":
            self.__initial_state__ = [
                [' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ']
            ]
        else:
            print("Invalid game_mode")

    def change_game_mode(self, new_game_mode):
        self.__game_mode__ = new_game_mode

    def set_button_pushed_command(self, command):
        self.__command_button_pushed__ = command

    def set_highscore_list(self, highscore_list):
        self.__highscore_list__ = highscore_list

    def create_window(self):
        if self.__game_mode__ == "tictactoe":
            self.__window_title__ = "Tic Tac Toe"
        elif self.__game_mode__ == "dame":
            self.__window_title__ = "Dame"
        else:
            print("GameWindow.create_window: Invalid game mode")
            return

        app = App(title="Tic Tac Toe", height=800, width=500)
        app.bg = "#D9D9D9"

        header = Box(app, align="top", width="fill")
        header.tk.configure(padx=10, pady=10)
        help_button_box = Box(header, width="fill")

        container = Box(app, layout="grid", height="fill")
        highscore_box = Box(header)
        game_ui_box = Box(container, grid=[1, 1])

        highscore = Highscore(highscore_box, self.__highscore_list__)

        if self.__game_mode__ == "tictactoe":
            game_ui = TicTacToe(game_ui_box, self.__initial_state__, self.__command_button_pushed__)
        elif self.__game_mode__ == "dame":
            raise NotImplemented("Dame wurde noch nicht implementiert")
        else:
            print("GameWindow.create_window: Invalid game mode")
            return

        help_button = __create_help_button__(help_button_box)

        container.tk.pack_configure(expand=True)
        # help_button_box.tk.pack_configure(anchor="ne", padx=10, pady=10)

        app.display()
