'''
Things are the things that exist in the game world.
They can be props, entities, or containers.
They have a number of default behaviors, which can be overridden.
Default behaviors:
- take
- attack
- drop
- use
'''
class Thing():
    def __init__(self) -> None:
        pass