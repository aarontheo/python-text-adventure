from classes import *
import curses

def main(screen:curses.window):
    # room1 = Room('rooms/cave1.json')
    # # print(room1.__getstate__())
    
    # obj1 = Thing('things/rock.json')
    # # print(obj1.__getstate__())
    # obj2 = Thing("things/rock.json")
    # print(obj1.attack(obj2))
    # print(obj1.attack(obj2))
    # print(obj2.look())
    
    # Now, to make the UI...
    
    # need to make a text input box
    
    # need to make a text output box
    
    # need to make an info box, show the current location, inventory, health status, etc.
    pass
    
if __name__ == '__main__':
    curses.wrapper(main)