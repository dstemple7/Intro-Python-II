# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.items = items
    
    # need a method to be able to add an item to the room
    def addItem(self, itemName):
        pass
    
    # need a method to be able to remove an item from the room
    def removeItem(self, itemName):
        pass

    def __str__(self):
        return f"room {self.name} which is described as: {self.description} and has the following items available: {self.items}"
