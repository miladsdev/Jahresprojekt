from guizero import PushButton, Box, App, info, Window
import os
from ui.dame_ui import DameUI
from ui.highscore import Highscore
from ui.tictactoe_ui import TicTacToe


class GameWindow:

    def __init__(self,
                 master,
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
        self.app = None
        self.__master__ = master
        self.__window_title__ = None
        self.__game_mode__ = game_mode
        self.__initial_state__ = initial_state
        self.__command_button_pushed__ = command_button_pushed
        self.__highscore_list__ = highscore_list
        self.__game_ui__ = None

    def __set_initial_state__(self):
        if self.__initial_state__ is not None:
            return
        if self.__game_mode__ == "dame":
            self.__initial_state__ = [
                ['X', ' ', 'X', ' ', 'X', ' '],
                [' ', 'X', ' ', 'X', ' ', 'X'],
                [' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' '],
                ['O', ' ', 'O', ' ', 'O', ' '],
                [' ', 'O', ' ', 'O', ' ', 'O']
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

    def __create_help_button__(self, master):
        help_button = PushButton(master, text="?", align="right", image=os.path.abspath("ui/assets/images/help.png"), width=30, height=30,
                                 command=self.__command_help_button__)
        help_button.tk.config(relief="flat", cursor="hand2")
        return help_button

    def __command_help_button__(self):
        tictactoe_rules = "- Jeder Spieler kann einen Stein pro Zug legen \n- Die Steine können überall auf dem " \
                          "Spielfeld gelegt werden \n- Gewonnen hat, wer zuerst 4 Steine vertikal, horizontal oder " \
                          "diagonal in einer Reihe hat \n- Sind alle Felder belegt bevor es einen Gewinner gab ist es " \
                          "Unentschieden"
        dame_rules = "- Jeder Spieler hat 8 steine\n- Die Steine dürfen nur auf dunklen Feldern liegen\n- Am Start " \
                     "liegen die Steine auf den ersten zwei Reihen des Spielfelds\n- Die Steine sind nur diagonal zu " \
                     "Bewegen\n- Gegnerische Steine schlägt man durch überspringen, wenn das Feld dahinter frei " \
                     "ist\n- Ein weiterer Stein kann übersprungen werden, sollte das Feld dahinter frei sein\n- " \
                     "Übersprungene Steine werden vom Spielfeld genommen\n- Eigene Steine sind nicht überspringbar\n- " \
                     "Gewonnen hat, wer einen Stein auf der gegnerischen Startlinie platziert\n- Verloren hat, " \
                     "wer keine Steine oder mögliche Züge mehr hat"
        if self.__game_mode__ == "tictactoe":
            rules = tictactoe_rules
        elif self.__game_mode__ == "dame":
            rules = dame_rules
        else:
            rules = "There is no such game mode"
        info(master=self.app, title="Rules", text=rules)

    def create_window(self):
        if self.__game_mode__ == "tictactoe":
            self.__window_title__ = "Tic Tac Toe"
        elif self.__game_mode__ == "dame":
            self.__window_title__ = "Dame"
        else:
            print("GameWindow.create_window: Invalid game mode")
            return

        self.app = Window(self.__master__, title="Tic Tac Toe", height=600, width=500)
        self.app.bg = "#D9D9D9"

        header = Box(self.app, align="top", width="fill")
        header.tk.configure(padx=10, pady=10)
        help_button_box = Box(header, width="fill")

        container = Box(self.app, layout="grid", height="fill")
        highscore_box = Box(header)
        game_ui_box = Box(container, grid=[1, 1])

        highscore = Highscore(highscore_box, self.__highscore_list__)

        if self.__game_mode__ == "tictactoe":
            self.__game_ui__ = TicTacToe(game_ui_box, self.__initial_state__, self.__command_button_pushed__)
        elif self.__game_mode__ == "dame":
            self.__game_ui__ = DameUI(game_ui_box, self.__initial_state__, self.__command_button_pushed__)
        else:
            print("GameWindow.create_window: Invalid game mode")
            return

        help_button = self.__create_help_button__(help_button_box)

        container.tk.pack_configure(expand=True)

        self.app.show(wait=True)
        # app.display()
