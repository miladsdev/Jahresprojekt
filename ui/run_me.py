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


# Dummy funktion on button click
def push_button(x, y, ai_move):
    print(x, y)
    ai_move(x+1, y+1)

    return True


# List fetched from database
highscore_list = ["Hasipupsi", "Peter Hans", "Elon Musk", "Beyoncé", "Hasipupsi", "Peter Hans", "Elon Musk", "Beyoncé"]

game_window = GameWindow(game_mode="tictactoe",
                         command_button_pushed=push_button,
                         highscore_list=highscore_list,
                         # initial_state=board
                         )
game_window.create_window()
