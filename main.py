from classes.Room import *
from classes.Registry import *

def main():
    room1 = Room('rooms/cave1.json')
    print(dir(room1))

if __name__ == '__main__':
    main()