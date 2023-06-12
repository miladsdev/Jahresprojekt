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
            title_box = Box(box, grid=[0, 0, 2, 1], border=True, width=300, height=40)
            title_box.bg = "#ffffff"
            title = Text(title_box, text="Bestenliste")
            title.text_size = 18
            for i, entry in enumerate(self.highscore_list):
                if i >= 10:
                    return
                x = 0
                y = i + 1
                if i >= 5:
                    x = 1
                    y = (i % 5) + 1
                text_box = Box(box, grid=[x, y], align="left", border=True, width=150, height=30)
                text_box.bg = "#ffffff"
                text_value = str(i+1) + ". " + entry
                icon = ""
                if i < 3:
                    icons = ['🥇', '🥈', '🥉']
                    icon = icons[i]
                Text(text_box, text=text_value, align="left")
                Text(text_box, text=icon, align="right")
