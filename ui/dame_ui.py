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

    def __push_button__(self, button, command, x, y):
        if ((x+y) % 2) == 1:
            return
        if self.__selected_from_position__ is None:
            button.bg = "lightblue"
            self.__selected_from_position__ = button
        elif self.__selected_from_position__ == button:
            button.bg = "grey"
            self.__selected_from_position__ = None
        else:
            # TODO: Validate the move
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
