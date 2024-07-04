import curses

class CurseWindow():
    def __init__(self, width, height:int, x:int, y:int):
        self.window = curses.newwin(height, width, y, x)
        self.border = False
        
    def border(self):
        self.window.border()
        
    def addstr(self, *args):
        match args:
            case (int() as x, int() as y, str() as text, *rest):
                self.window.addstr(y, x, text, *rest)
            case (str() as text, *rest):
                self.window.addstr(text, *rest)
        
    def refresh(self):
        self.window.refresh()
        
    def drawstr(self, x, y, string):
        self.addstr(x, y, string)
        self.refresh()

class Pane(CurseWindow):
    def __init__(self, width:int, height:int, x:int, y:int):
        super().__init__(width, height, x, y)
        if width < 3 or height < 3:
            raise BaseException("Bordered Panes must have a minimum height and width of 3!")
        self.border()
        
    def addstr(self, *args):
        match args:
            case (str() as text, *rest):
                super().addstr(1, 1, *args)
            case _:
                super()
