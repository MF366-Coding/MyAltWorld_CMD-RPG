# Rooms for MyAltWorld

import commands
from adventurelib import *
from clsCmd import clear


class House_1:
    # attributes for your house
    ur_bedroom = Room("""
					OH MY GOD!!
					How could this happen?

					You're in your bedroom!!!!
					It looks messy by the way...

					There is only one exit to south.
					Unless you could jump from the window...
					I mean it's just a one floor house so...
					""")
    corridor_2 = Room("""
					How interesting!

					By leaving your room, you reach the main corridor.

					There is nothing to the right.
					Why would it?
					""")


current_room = None
Room.can_yell = True
Room.can_brush = False
