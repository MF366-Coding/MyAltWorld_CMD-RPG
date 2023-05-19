from adventurelib import *
from clsCmd import clear
from rooms import *

@when("scream")
@when("yell")
@when("shout")
def scream():
    if current_room.can_yell == True:
        say("""
            You yell with all you might!
            
            Nobody heard anything, probably...
            """)
    else:
        say("""
            You wanted to scream...
            
            But something kept you from doing so...
            """)
        
        