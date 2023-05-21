from adventurelib import *
import adventurelib as alib
import random
from clsCmd import clear as clearing

# the room youre in
current_room = None

# commands
@when("i got bitches")
def no_bitches():
    say("""
It's rude to lie...

YOU GOT NO BITCHES LMFAO!
""")

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


@when("clear mind")
@when("clear")
@when("deep breath")
@when("clear thoughts")
def clear():
    clearing()


@when('look')
@when("look around")
def look():
    say(current_room)


@when('north', direction='north')
@when('south', direction='south')
@when('east', direction='east')
@when('west', direction='west')
@when('north', direction='north')
@when('south', direction='south')
@when('east', direction='east')
@when('west', direction='west')
def go(direction):
    global current_room

    room = current_room.exit(direction)
    if room:
        current_room = room
        print(f'You go {direction}.')
        look()
    else:
        say("""Hmmm...
            There's nothing that way!

            Let's take another look at
            the room...


            """)
        look()

def none_command_matches(command):
    print(random.choice([
        f"Well, I don't know '{command}'!",
        f"Maybe you should use '{command}' in another game?!",
        f"Why do you give me commands I don't understand?",
        f"Guess what! I can't do '{command}'...",
        f"Look, I'm no ChatGPT, ok? I can't do '{command}'.",
        f"What? What's '{command}'?!",
        f"I can't guess how to do '{command}'...",
        f"I apologize but I'm not an AI! I can't do that...",
        f"'{command}'. I dunno what that is...",
        f"'{command}', '{command}'. Can't find it in my infinite knowledge.",
        f"I'm not a NPC! Don't give me '{command}'"
    ]))

alib.no_command_matches = none_command_matches

# rooms for myaltworld
room_3 = Room("""
You woke up and...          


OH MY GOD!!
How could this happen?


You're in your bedroom!!!!

It looks messy by the way...


There are clothes everywhere!

If your mother was still here...

She'd tell you to clean up this mess...

But she isn't... here...


There is only one exit to south.

Unless you could jump from the window...

I mean it's just a one floor house so...

""")

room_4 = Room("""room coming tomorrow lel""")

room_5 = Room("""
How interesting!

By leaving your room, you reach the main corridor.

To the RIGHT, there's your mother's bedroom.
It's always locked. Dad sleeps in the couch...
He's too afraid of his loss...
You too are...

To the LEFT, the amazing... bathroom...

To SOUTH, you can take a glance at your huge
dining room...

There is nothing else to say, except for some
paitings covered by spider webs...

""")

# atributes
room_5.north = room_3
room_3.south = room_5

Room.can_yell = True
Room.can_brush = False


if __name__ == '__main__':
    current_room = room_3
    clear()
    with open("init.txt", 'r', encoding='utf-8') as initTextFile:
        initText = initTextFile.read()
        initTextFile.close()
    print(initText)
    print("\n\n\t\t\t\t\t< THE ADVENTURE BEGINS >\n\n\n")
    say(room_3)
    start(help=False) # used to load the game
