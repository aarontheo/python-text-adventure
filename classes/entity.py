import json
import importlib
import inspect
from types import MethodType


'''
Things are the pieces of the game that are acted upon.
to perform an action on a thing, simply call the action as a verb with the indirect/instrumental object as the argument.
Ex. Attack troll with sword
troll.attack(sword)

All action methods should return a string, which can be displayed to the user.
Unknown actions called on an object return "I don't know how to {verb} the {self.name}."
'''
class Thing():
    def __init__(self, json_path:str) -> None:
        self.name = 'thing'
        self.desc = 'a cool thing'
        self.shortdesc = 'a thing'
        
        self.actions = dict()
        
        with open(json_path, 'r') as file:
            JSON_data = json.load(file)
        
        for attr in JSON_data:
            setattr(self, attr, JSON_data[attr])
            
        trait_names = JSON_data['traits']
        for trait in trait_names:
            self.add_trait(trait)
    
    # def get_action(self, verb:str) -> function:
    #     return self.actions[verb]

    # def get_action(self, verb:str):
    #     try:
    #         return self.__getattribute__(verb)
    #     except:
    #         return lambda *args: f"I don't know how to {verb} the {self.name}."
            
    # def __getattribute__(self, attr:str):
    #     return object.__getattribute__(self, attr)
    
    def __getattr__(self, verb:str):
        return lambda *args: f"I don't know how to {verb} the {self.name}."
    
    def add_trait(self, trait_name:str):
        # get the trait's class
        cls = get_class(f"classes.traits.{trait_name}")
        
        # verify that the Thing has all the needed attributes.
        assert_instance_attributes(cls, self)
        
        # get all methods from the trait class
        methods = get_class_methods(cls)
        add_methods_to_action_dict(self, methods)
    
    def add_traits(self, traits:list):
        for trait in traits:
            self.add_trait(trait)
    
    # def has_trait(self, trait):
    #     return trait in self.traits
    
    def harm(self, damage:int):
        return f"You attack the {self.name}, to no avail."
    
    def look(self):
        return self.desc.capitalize()
    

"""
These are functions that manipulate class methods, allowing for traits rather than inheritance.
"""
def hasattr(obj:object, name:str):
    return name in obj.__dict__

def get_class(class_path:str) -> type:
    module_name, class_name = class_path.rsplit('.', 1)
    module = importlib.import_module(module_name, package="classes")
    cls = getattr(module, class_name)
    return cls

def get_class_methods(cls:type) -> list[classmethod]:
    methods = []
    for name, attr in cls.__dict__.items():
        if inspect.isfunction(attr) or inspect.ismethod(attr):
            methods.append((name, attr))
    return methods

def assert_instance_attributes(cls:type, instance:object):
    if attrs := cls.req_attributes:
        for attr in attrs:
            if not hasattr(instance, attr):
                raise MissingAttributeException(instance, attr)

def add_methods_to_instance(instance:object, method_list:list):
    for (name, method) in method_list:
        bound_method = MethodType(method, instance)
        setattr(instance, name, bound_method)
        
def add_methods_to_action_dict(instance:Thing, method_list:list):
    if not hasattr(instance, 'actions'):
        setattr(instance, 'actions', dict())
    for (name, method) in method_list:
        instance.actions[name] = method

class MissingAttributeException(Exception):
    def __init__(self, obj, attr) -> None:
        super().__init__(f"Object {obj} is missing attribute '{attr}'")

