# Write a class to hold player information, e.g. what room they are in
# currently.

from item import Item

class Player:
  def __init__(self, location, item=[]):
    self.location = location
    self.item = item

  def pickupItem(self, itemName):
    # check if item exists in the room
    # append item to self.items list
    self.item.append(itemName)
    # remove it from the current room inventory
    self.location.item.pop(itemName)

  def dropItem(self, itemName):
    pass
    # check if item exists in the player's inventory
    # append item to room items list
    # remove it from the players inventory