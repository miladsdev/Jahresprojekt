from ui.game_window import GameWindow

# Run this file to see UI
# For now works only with tictactoe


# (Initial) State of the board
board = [
    [' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', 'O', ' '],
    [' ', 'X', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ']
]

turn = "X"


# Dummy funktion on button click
def push_button(pushed_button, x, y):
    global turn
    pushed_button.text = turn
    print(x, y)
    if turn == "X":
        pushed_button.image = "assets/images/red.png"
        turn = "O"
    else:
        pushed_button.image = "assets/images/yellow.png"
        turn = "X"


# List fetched from database
highscore_list = ["Hasipupsi", "Peter Hans", "Elon Musk", "Beyoncé", "Hasipupsi", "Peter Hans", "Elon Musk", "Beyoncé"]

game_window = GameWindow(game_mode="tictactoe",
                         command_button_pushed=push_button,
                         highscore_list=highscore_list)
game_window.create_window()
