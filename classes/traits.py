import importlib
import inspect
from types import MethodType


"""
Traits are classes that implement methods, which add behaviors that can be used with Things.
Traits also have required attributes.
"""
class Trait():
    pass
        
class HAS_HP():
    req_attributes = [
        'hp',
        'maxhp'
    ]
    
    def harm(self, damage:int):
        self.hp -= damage
        return f"The {self.name} is {self.status()}."
        
    def status(self):
        health = self.hp/self.maxhp
        if 0.8 < health <= 1:
            return "pristine"
        elif 0.5 < health <= 0.8:
            return "battered"
        elif 0 < health <= 0.5:
            return "damaged"
        else:
            return "destroyed"
        
    def look(self):
        if self.hp/self.maxhp < 1:
            return f"{self.desc}. It is {self.status()}."
        else:
            return (self.desc+'.').capitalize()
            

class IS_LIVING():
    req_attributes = HAS_HP.req_attributes
    
    def status(self):
        health = self.hp/self.maxhp
        if 0.8 < health <= 1:
            return "healthy"
        elif 0.5 < health <= 0.8:
            return "battered"
        elif 0 < health <= 0.5:
            return "bloodied"
        else:
            return "dead"

class IS_WEAPON():
    req_attributes = [
        'damage',
        'size',
    ]
    
    def attack(self, dobj):
        return f"You attack the {dobj.name} with the {self.name}.\n" + dobj.harm(self.damage)

class IS_EDIBLE():
    req_attributes = [
        'hp_restored'
    ]

    def eat(self, actor):
        actor.heal(self.hp_restored)
        return f"You eat the {self.name}, and feel {actor.status()}."

class HAS_INVENTORY():
    req_attributes = [
        'capacity',
    ]
    
    def remaining_capacity(self):
        filled_capacity = 0
        for item in self.inventory:
            filled_capacity += item.size()
        return self.capacity - filled_capacity
    
    def put(self, item):
        if not hasattr(item, "size"):
            return "It won't budge."
        if self.remaining_capacity() - item.get_size() >= 0:
            self.inventory.add(item)
            return f"Put the {item.name} into the {self.name}"
        else:
            return "Not enough room!"