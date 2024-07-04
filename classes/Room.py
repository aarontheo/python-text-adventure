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
            # print(JSON_data)
        
        for attr in JSON_data:
            setattr(self, attr, JSON_data[attr])

    def __getattr__(self, name: str):
        return (False, name, "NoAttribute")