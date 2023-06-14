from guizero import info

from ui.board_game import BoardGame


class DameUI(BoardGame):
    def __init__(self, master, board_data=None, on_button_push=None):
        if board_data is None:
            board_data = [
                ['X', ' ', 'X', ' ', 'X', ' '],
                [' ', 'X', ' ', 'X', ' ', 'X'],
                [' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' '],
                ['O', ' ', 'O', ' ', 'O', ' '],
                [' ', 'O', ' ', 'O', ' ', 'O']
            ]
        super().__init__(master, board_data, on_button_push)
        self.__selected_from_position__ = None
        self.__selected_to_position__ = None
        self.__button_coordinates__ = {
            "x1": None,
            "y1": None,
            "x2": None,
            "y2": None
        }

    def __push_button__(self, button, command, x, y, ai_move):
        if ((x + y) % 2) == 1:
            return
        if self.__selected_from_position__ is None:
            # Set first button clicked
            self.__button_coordinates__["x1"] = x
            self.__button_coordinates__["y1"] = y

            button.bg = "lightblue"
            self.__selected_from_position__ = button
        elif self.__selected_from_position__ == button:
            # Reset button clicked
            button.bg = "grey"

            self.__button_coordinates__["x1"] = None
            self.__button_coordinates__["y1"] = None
            self.__selected_from_position__ = None
        else:
            # Set second button clicked
            self.__button_coordinates__["x2"] = x
            self.__button_coordinates__["y2"] = y
            # TODO: Validate the move
            # coords = self.__button_coordinates__
            # is_move_valid = command(coords["x1"], coords["y1"], coords["x2"], coords["y2"], ai_move)
            is_move_valid = True
            if is_move_valid:
                self.__selected_to_position__ = button
                self.__selected_from_position__.bg = "grey"
                image = self.__selected_from_position__.image
                self.__selected_to_position__.image = None
                self.__selected_to_position__.image = image
                self.__selected_to_position__.width = 50
                self.__selected_to_position__.height = 50
                self.__selected_from_position__.image = None
                self.__selected_from_position__.text = " "
                self.__selected_from_position__.width = 50
                self.__selected_from_position__.height = 50
                self.__selected_to_position__ = None
                self.__selected_from_position__ = None
            else:
                info(master=self.master, title="Invalid move", text="Das kannst du nicht machen!")

    def ai_move(self, x, y):
        # TODO: Implement AI move visualization
        pass
