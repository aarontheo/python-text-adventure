import json

'''
Has the following attributes:
desc: str
shortdesc: str
doors: dictionary of doors
contains: list of things in the room
'''
class Room():
    def __init__(self, json_path:str) -> None:
        with open(json_path, 'r') as file:
            JSON_data = json.load(file)
            self.contents = list()
            # print(JSON_data)
        
        for attr in JSON_data:
            setattr(self, attr, JSON_data[attr])
            
    def look(self) -> str:
        return self.desc

    def __getattr__(self, name: str):
        return (name, "NoAttribute")
    
    def __contains__(self, item):
        return item in self.contents