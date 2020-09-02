from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player('outside')
print(room[player.location].name)
print(room[player.location].description)

def goNorth():
    room[player.location] = room[player.location].n_to
    if room[player.location] != 0:
        print("\n")
        print(room[player.location].name)
        print(room[player.location].description)

def goEast():
    room[player.location] = room[player.location].e_to
    if room[player.location] != 0:
        print("\n")
        print(room[player.location].name)
        print(room[player.location].description)

def goSouth():
    room[player.location] = room[player.location].s_to
    if room[player.location] != 0:
        print("\n")
        print(room[player.location].name)
        print(room[player.location].description)

def goWest():
    room[player.location] = room[player.location].w_to
    if room[player.location] != 0:
        print("\n")
        print(room[player.location].name)
        print(room[player.location].description)

# print(player)


# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# print(player.room)
# * Waits for user input and decides what to do.
# If the user enters "q", quit the game.
#
# If the user enters a cardinal direction, attempt to move to the room there.
selection = ""

while selection != None:

    selection = str(input(
        "What would you like to do? To move, enter the cardinal directions or type q to exit the game "))

    try:

        if selection == 'q':
            break

        elif selection == 'n':
            goNorth()

        elif selection == 'e':
            goEast()

        elif selection == 's':
            goSouth()

        elif selection == 'w':
           goWest()

        else:
            print("\n")
            print("Please input only the letter n, e, s, or w of the cardinal direction you'd like to move or type q to exit the game ")
    
    except AttributeError:
        print("\n")
        print("Sorry, you've hit a wall, try another direction")

# Print an error message if the movement isn't allowed.
#
# branch table
# 
# create a dictionary with n/s/e/w as keys and then make key equal to whatever function
# dic[selection]()
# "e": goEast
#
# Do you have a big if-elif block in your cpu_run() function? Is there a way to better modularize your code? There are plenty of them!
# What is the time complexity of the if-elif cascade? In the worst case, we're going to have to check the value in IR against all of the possible opcode values. This is O(n). It would be a lot better if it we an O(1) process...
# One option is to use something called a branch table or dispatch table to simplify the instruction handler dispatch code. This is a list or dictionary of functions that you can index by opcode value. The upshot is that you fetch the instruction value from RAM, then use that value to look up the handler function in the branch table. Then call it.
# Example of a branch table:
# OP1 = 0b10101010
# OP2 = 0b11110000
# class Foo:
#     def __init__(self):
#         # Set up the branch table
#         self.branchtable = {}
#         self.branchtable[OP1] = self.handle_op1
#         self.branchtable[OP2] = self.handle_op2
#     def handle_op1(self, a):
#         print("op 1: " + a)
#     def handle_op2(self, a):
#         print("op 2: " + a)
#     def run(self):
#         # Example calls into the branch table
#         ir = OP1
#         self.branchtable[ir]("foo")
#         ir = OP2
#         self.branchtable[ir]("bar")
# c = Foo()
# c.run()