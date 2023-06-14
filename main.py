from guizero import App, Box, PushButton, Text, warn

from dame.dame import Game
from database.db import Datenbank
from ui.game_window import GameWindow
from ui.login import Login


class GameMode:
    def __init__(self, master, start_game_mode_command, back_command):
        self.back_command = back_command
        self.master = master
        self.start_game_mode_command = start_game_mode_command
        self.box = None
        self.selected_game_mode = None
        self.__game_modes__()

    def __game_modes__(self):
        self.box = Box(self.master)
        Text(self.box, text="Wähle ein Spielmodus")
        PushButton(self.box, text="Dame", command=self.start_game_mode_command, args=["dame"])
        PushButton(self.box, text="TicTacToe", command=self.start_game_mode_command, args=["tictactoe"])
        PushButton(self.box, text="Zurück", command=self.go_back)
        self.box.hide()

    def go_back(self):
        self.back_command()
        self.hide_game_modes()

    def show_game_modes(self):
        self.box.show()

    def hide_game_modes(self):
        self.box.hide()


db = Datenbank()


def back_to_home_screen():
    home_screen.show()


def show_login():
    home_screen.hide()
    login_screen.show_login()


def show_game_mode():
    home_screen.hide()
    game_mode.show_game_modes()


user = None


def perform_login(username, password):
    is_account_valid = db.login(username, password)
    global user
    if is_account_valid:
        user = username
        login_screen.hide_login()
        game_mode.show_game_modes()
    else:
        user = None
        warn(title="Fehler", text="Falsche Anmeldedaten")


def button_pushed(x1, y1, x2, y2):
    return dame.make_move(x1, y1, x2, y2)


dame = Game()


def start_game(game_mode):
    game = GameWindow(game_mode=game_mode, command_button_pushed=button_pushed, master=app)
    game.create_window()


app = App(title="Welcome")
home_screen = Box(app)

login_screen = Login(app, back_to_home_screen, perform_login)

game_mode = GameMode(app, start_game, back_to_home_screen)

login_button = PushButton(home_screen, text="Login?", command=show_login)
guest_button = PushButton(home_screen, text="Weiter als Gast", command=show_game_mode)
app.display()
