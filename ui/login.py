from guizero import Box, TextBox, PushButton


class Login:
    def __init__(self, master, back_command, login_command):
        self.master = master
        self.back_command = back_command
        self.login_command = login_command
        self.box = None
        self.__login__()
        self.__username__ = None
        self.__password__ = None

    def __login__(self):
        self.box = Box(self.master)
        self.__username__ = TextBox(self.box)
        self.__password__ = TextBox(self.box, hide_text=True)
        PushButton(self.box, text="Login", command=self.__perform_login__,
                   args=[self.__username__, self.__password__])
        PushButton(self.box, text="Zurück", command=self.go_back)
        self.box.hide()

    def __perform_login__(self, username_field, password_field):
        username = username_field.value
        password = password_field.value
        self.login_command(username, password)

    def go_back(self):
        self.back_command()
        self.hide_login()

    def show_login(self):
        self.box.show()

    def hide_login(self):
        self.box.hide()
