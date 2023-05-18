from os import system as cmd_open
from sys import platform as pf

def clear():
    if pf == 'win32':
        clearCmd = 'cls'
        
    elif pf == 'linux' or pf == 'darwin':
        clearCmd = 'clear'
    
    else:
        clearCmd = 'clear'
    
    cmd_open(clearCmd)
