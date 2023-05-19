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
                        """)
    corridor_2 = Room("""
                      How interesting!
                      
                      By leaving your
                      """)


current_room = None
Room.can_yell = True
Room.can_brush = False
	