What if... Instead of having classes that inherit from each other, I have a base thing class which is created from a JSON object, and I have classes with methods that I enumerate and add to the object? I could literally assemble classes from whatever components I want.

Example: I have a Thing that I want to have an inventory and be takeable. 
So, I give it the flags HAS_INVENTORY and IS_TAKEABLE.
During the Thing's initialisation, I look through the flags, each of which is a separate class.
the HAS_INVENTORY class has methods for capacity() and store(object),
the IS_TAKEABLE class has methods for take() and put(object).

Rather than having the limitations of inheritance, I can compose custom-built classes on the fly! I will add a \_\_hasattr\_\_() method to Thing, so that if an unknown method is called, it can give back a message, like "I don't know how to {action} with {thing.name}."

Of course, for simplicity I can still use object inheritance to simplify certain things, like doors, rooms, and possibly actors. But it's so good!!
