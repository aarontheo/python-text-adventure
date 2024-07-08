from classes import Player, Registry, Room, Thing
from parsing import simple_parse
import glob
import json

class DungeonMaster():
    '''
    A Dungeon Master keeps track of the world, the players, and the Things in the world,
    and gives responses when players ask it questions about the world or perform actions.
    It also continuously prompts
    '''
    def __init__(self, json_path: str):
        self.rooms = Registry(Room)
        self.items = Registry(Thing)
        self.player = Player('content/actors.player.json')
        self.config = json.load(open('config.json'))
        self.player_location_id = self.config['start_room']
        
    def run_command(self, command:str):
        if command == 'look':
                return self.rooms[self.player_location_id].look()
        else:
            match parsed_command := simple_parse(command):
                case (verb,):
                    return self.player.__getattribute__(verb)()
                case (verb, dobj):
                    pass
                case (verb, dobj, iobj):
                    pass
        
    def start_game_loop(self, prompt:str):
        output = self.rooms[self.player_location_id].look()
        while True:
            print(output)
            command = input(prompt).strip()
            print(
                self.run_command(command)
                )
        
    def item_is_present(self, id) -> bool:
        # check if the item is present
        # first check the player's inventory
        # then check the room
        pass
    
    def find_thing(self, thing_id):
        # check the player's inventory
        # check the room's contents
        # check the contents of open containers in the room
        # return a message of 'there is no ______ here'
        pass
    
    def do_action(self):
        pass