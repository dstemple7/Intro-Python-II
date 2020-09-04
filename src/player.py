# Write a class to hold player information, e.g. what room they are in
# currently.

from item import Item

class Player:
  def __init__(self, location):
    self.location = location
    self.items = []

  def pickupItem(self, item_name, item_description):
    # check if item exists in the room
    # append item to self.items list
    self.items.append(Item(item_name, item_description))
    self.location.items.remove(Item(item_name, item_description))
    # remove it from the current room inventory
    # self.location.items.pop(item)

  def dropItem(self):
    self.items.remove(self.items[0])
    self.location.items.append(self.items[0])
    # check if item exists in the player's inventory
    # append item to room items list
    # remove it from the players inventory