from classes import *

def main():
    room1 = Room('rooms/cave1.json')
    # print(room1.__getstate__())
    
    obj1 = Thing('things/rock.json')
    # print(obj1.__getstate__())
    obj2 = Thing("things/rock.json")
    print(obj1.attack(obj2))
    print(obj1.attack(obj2))
    print(obj2.look())
    
if __name__ == '__main__':
    main()