import curses
import curses.textpad
from time import sleep

class TextPane():
    def __init__(self, width:int, height:int, x:int, y:int, border=False) -> None:
        if border:
            self.border_win = curses.newwin(height, width, y, x)
            self.window = curses.newwin(height-2, width-2, y+1, x+1)
        else:
            self.window = curses.newwin(height, width, y, x)
            self.border_win = None
        
    def refresh(self):
        self.window.refresh()
                
    def clear(self):
        self.window.clear()
        
    def print(self, x, y, text):
        self.window.addstr(text+'\n')
        
        
    

def main(screen:curses.window):
    # !!!DO NOT REMOVE THE LINE BELOW!!!
    screen.refresh() # I don't know why this is needed, but it is.
    # =====================
    # Window Specs
    # =====================
    # CSS much?
    HEIGHT, WIDTH = curses.LINES, curses.COLS
    
    INFO_Y, INFO_X = 0, 0
    INFO_WIDTH = WIDTH//3
    INFO_HEIGHT = HEIGHT
    
    INPUT_HEIGHT = 3
    OUTPUT_Y, OUTPUT_X = 0, INFO_WIDTH
    OUTPUT_WIDTH = WIDTH-INFO_WIDTH
    OUTPUT_HEIGHT = HEIGHT-INPUT_HEIGHT
    
    INPUT_Y, INPUT_X = HEIGHT-INPUT_HEIGHT, INFO_WIDTH
    INPUT_WIDTH = OUTPUT_WIDTH
    # =====================
    # Window Initialization
    # =====================
    win_info = curses.newwin(INFO_HEIGHT, INFO_WIDTH, INFO_Y, INFO_X)
    win_output = curses.newwin(OUTPUT_HEIGHT, OUTPUT_WIDTH, OUTPUT_Y, OUTPUT_X)
    win_input = curses.newwin(INPUT_HEIGHT, INPUT_WIDTH, INPUT_Y, INPUT_X)
    
    win_info.border()
    win_info.addstr(1, 1, "This is the info panel!")
    win_info.refresh()
    win_output.border()
    win_output.addstr(1, 1, "This is the output panel!")
    win_output.addstr(1, 1, "More text")
    win_output.refresh()
    win_input.border()
    win_input.addstr(1, 1, "This is the input panel!")
    # win_input.addch(1,1, '>')
    # curses.cbreak()
    # win_input.getstr(1, 2)
    # win_input.refresh()
    
    
    screen.getch()
    win_output.refresh()
    screen.getch()
    

if __name__ == '__main__':
    curses.wrapper(main)