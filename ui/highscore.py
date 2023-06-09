from guizero import Box, Text


class Highscore:

    def __init__(self, master, highscore_list=None):
        self.highscore_list = highscore_list
        self.master = master
        self.create_highscore()

    def create_highscore(self):
        box = Box(self.master, layout="grid")
        if not self.highscore_list:
            title = Text(box, text="Highscore ist leer", grid=[0, 0])
            title.text_size = 13
        else:
            title = Text(box, text="Bestenliste", grid=[0, 0, 2, 1])
            title.text_size = 18
            for i, entry in enumerate(self.highscore_list):
                if i >= 10:
                    return
                x = 0
                y = i + 1
                if i >= 5:
                    x = 1
                    y = (i % 5) + 1
                Text(box, text=str(i+1) + ". " + entry, grid=[x, y], align="left")
