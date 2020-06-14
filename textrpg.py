# Python Text RPG
# Luiz Otavio Ibrahim

import cmd
import textwrap
import sys
import os
import time
import random

screen_width = 100

##### Player Setup #####
class player:
    def __init__(self):
        self.name =''
        self.job = ''
        self.hp = 0
        self.mp = 0
        self.status_effects = []
        self.location = 'b2'
        self.game_over = False
myPlayer = player()

##### Title Screen #####

def title_screen_selections():
    option = input("> ")
    if option.lower() == ("play"):
        setup_game() # placeholder until written
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower() == ("quit"):
        system.exit() # End cmd 
    while option.lower() not in ['play', 'help', 'quit']:
        print("Please enter a valid command.")
        option = input("> ")
        if option.lower() == ("play"):
            setup_game() # placeholder until written
        elif option.lower() == ("help"):
            help_menu()
        elif option.lower() == ("quit"):
            system.exit() # End cmd 

def title_screen():
    os.system('cls')
    print('######################')
    print('# Welcome to the Text RPG! #')
    print('######################')
    print('  - Play -         ')
    print('  - Help -         ')
    print('  - Quit -         ')
    print('  - Luiz Otavio Ibrahim -         ')
    title_screen_selections()

def help_menu():
    os.system('cls')
    print('######################')
    print('# Welcome to the Text RPG! #')
    print('######################')
    print('-Use up, down, left right to move-')
    print('-Type your commands to do them-')
    print('-Use "look" to inspect something')
    print('-Good luck and have fun!-')
    title_screen_selections()

##### Map ######

"""
a1 a2 ... # Player Start At b2
-----------
|  |  |  |  a4
-----------
|  |  |  |  b4 ...
-----------
|  |  |  |
-----------
|  |  |  |
-----------

"""
ZONENAME = ''
DESCRIPTION = 'description'
EXAMINATION = 'examine'
SOLVED = False
UP = 'up', 'north'
DOWN = 'down', 'south'
LEFT = 'left', 'west'
RIGHT = 'right','east'


solved_places = {'a1': False, 'a2': False, 'a3': False, 'a4': False, 
                'b1': False, 'b2': False, 'b3': False, 'b4': False,  
                'c1': False, 'c2': False, 'c3': False, 'c4': False,  
                'd1': False, 'd2': False, 'd3': False, 'd4': False, 
                }

zonemap = {
    'a1':{
        ZONENAME: "a1",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'a1',
        DOWN: 'b1',
        LEFT: 'a1',
        RIGHT: 'a2'
    },
    'a2':{
        ZONENAME: "a2",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'a2',
        DOWN: 'b2',
        LEFT: 'a1',
        RIGHT: 'a3'
    },
    'a3':{
        ZONENAME: "a3",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'a3',
        DOWN: 'b3',
        LEFT: 'a2',
        RIGHT: 'a4'
    },
    'a4':{
        ZONENAME: "a4",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'a4',
        DOWN: 'b4',
        LEFT: 'a3',
        RIGHT: '',
    },
    'b1':{
        ZONENAME: "b1",
        DESCRIPTION : 'description',
        EXAMINATION : 'examine',
        SOLVED : False,
        UP : 'a1',
        DOWN : 'c1',
        LEFT : 'b1',
        RIGHT : 'b2'
    },
    'b2':{
        ZONENAME: 'HOME',
        DESCRIPTION : 'This is your home',
        EXAMINATION : 'Nothing has changed',
        SOLVED : False,
        UP : 'a2',
        DOWN : 'c2',
        LEFT : 'b1',
        RIGHT :'b3'
    },
    'b3':{
        ZONENAME: "b3",
        DESCRIPTION : 'description',
        EXAMINATION :'examine',
        SOLVED : False,
        UP : 'a3',
        DOWN : 'c3',
        LEFT : 'b2',
        RIGHT : 'b4'
    },
    'b4':{
        ZONENAME: "b4",
        DESCRIPTION : 'description',
        EXAMINATION : 'examine',
        SOLVED : False,
        UP : 'a4',
        DOWN : 'c4',
        LEFT : 'b3',
        RIGHT : 'b4'
    },
    'c1':{
        ZONENAME: "c1",
        DESCRIPTION : 'description',
        EXAMINATION : 'examine',
        SOLVED : False,
        UP : 'b1',
        DOWN : 'c1',
        LEFT : 'c1',
        RIGHT : 'c2'
    },
    'c2':{
        ZONENAME: "c2",
        DESCRIPTION : 'description',
        EXAMINATION :'examine',
        SOLVED : False,
        UP : 'b2',
        DOWN : 'c2',
        LEFT : 'c1',
        RIGHT :'c3'
    },
    'c3':{
        ZONENAME: "c3",
        DESCRIPTION : 'description',
        EXAMINATION : 'examine',
        SOLVED : False,
        UP : 'b3',
        DOWN : 'c3',
        LEFT : 'c2',
        RIGHT : 'c4'
    },
    'c4':{
        ZONENAME: "c4",
        DESCRIPTION : 'description',
        EXAMINATION :'examine',
        SOLVED : False,
        UP : 'b4',
        DOWN : 'c4',
        LEFT : 'b3',
        RIGHT : 'c4'
    },
}


##### Game Interactivuty #####
def print_location():
    print('\n' + ('#' * (4 + len(myPlayer.location))))
    print('# ' + myPlayer.location.upper() + ' #')
    print('# '+ zonemap[myPlayer.location][DESCRIPTION]+ ' #')
    print('\n' + ('#' * (4 + len(myPlayer.location))))

def prompt():
    print("\n" + "======================")
    print(" what would you like to do?")
    action = input("> ")
    acceptable_action = ['move','go', 'travel', 'walk', 'quit', 'examine', 'inspect', 'interact', 'look']
    while action.lower() not in acceptable_action:
        print("Unknown action, try again.\n")
        action = input("> ")
    if action.lower() == 'quit':
        sys.exit()
    elif action.lower() in ['move','go', 'travel', 'walk']:
        player_move(action.lower())
    elif action.lower() in ['examine', 'inspect', 'interact', 'look']:
        player_examine(action.lower())

def player_move(myAction):
    ask = 'Where would you like to move to? \n'
    dest = input(ask)
    if dest in ['up', 'north']:
        destination = zonemap[myPlayer.location][UP]
        movement_handler (destination)
    elif dest in ['left', 'west']:
        destination = zonemap[myPlayer.location][LEFT]
        movement_handler (destination)
    elif dest in ['right', 'east']:
        destination = zonemap[myPlayer.location][RIGHT]
        movement_handler (destination)
    elif dest in ['down', 'south']:
        destination = zonemap[myPlayer.location][DOWN]
        movement_handler (destination)

def movement_handler(destination):
    print("\n" + "You have moved to the " + destination + ".")
    myPlayer.location = destination
    print_location()

def player_examine(action):
    if zonemap [myPlayer.location][SOLVED]:
        print("You have already exhausted this zone.")
    else:
        print("Trigged a puzzle")

##### Game Functionality #####
def start_game():
    return

def main_game_loop():
    while myPlayer.game_over is False:
        prompt()
    # here gandle if puzzles have been solved, boss defeated, storyline.

def setup_game():
    os.system('cls')
    
    # name Colecting
    question1 = "Hello, What's your name\n"
    for character in question1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    player_name = input('> ')
    myPlayer.name = player_name


    # job handling
    question2 = "Hello, What job you wanna to play? \n"
    question2added = "You can play as a warrior, priest or mage \n"
    for character in question2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in question2added:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    player_job = input('> ')
    valid_jobs = ['warrior', 'mage', 'priest']
    if player_job.lower() in valid_jobs:
        myPlayer.jon = player_job
        print("You are now a " + player_job + "!\n")
    while player_job.lower() not in valid_jobs:
        player_job = input("> ")
        if player_job.lower() in valid_jobs:
            myPlayer_job = player_job
            print("You are now a" + player_job + "!\n")
                

    ## Player Stats
    if myPlayer.job is 'warrior':
        self.hp = 120
        self.mp = 20
    elif myPlayer.job is 'mage':
        self.hp = 40
        self.mp = 120
    elif myPlayer.job is 'mage':
        self.hp = 60
        self.mp = 60

    # Introduction

    question3 = "Welcome " + player_name + " the " + player_job + "\n"
    for character in question3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)

    speech1 = "Welcome to this fantasy world\n"
    speech2 = "I hope it greets you well\n"
    speech3 = "Just make sure you don't get too lost...\n"
    for character in speech1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in speech2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in speech3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    os.system('cls')
    print("##############")
    print("# Let's start now!")
    print("##############")
    main_game_loop()

title_screen()

