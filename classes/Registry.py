'''
A Registry is essentially a dictionary interface which allows objects to be registered under an identifier, such as a name or number.
'''
class Registry():
    def __init__(self, type:type) -> None:
        self.registered = dict()
        self.type = type
        
    def register(self, identifier, object:object):
        if identifier in self.registered.keys:
            raise KeyError("An object is already registered under this identifier. Use Registry.deregister to remove registered objects.")
        if not isinstance(object, self.type):
            raise TypeError(f"Object is of type: {object.__class__}; Registry is for objects of type {self.type} only.")
        self.registered[identifier] = object
        
    def deregister(self, identifier):
        self.registered.pop(identifier, None)
        
    def get(self, identifier):
        return self.registered.get(identifier, None)
    
    def __getitem__(self, id):
        return self.registered[id]
    
    def __contains__(self, id:str):
        return id in self.registered
    
    def __getitem__(self, id:str):
        return self.registered[id]