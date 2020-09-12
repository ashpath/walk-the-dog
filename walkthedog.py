__author__ = 'Victoria King'
'''
Known Issues:
- Entities (such as your dog, people, etc) don't have AI.
- Randomly Spawned Entities cannot currently occupy the same room
- Ran out of time for inventory system due to the recent house fire fiasco. Will continue to develop after project
due date in free time as a hobby project.

Everything else works so far.
'''


#import data for rooms (descriptions, what is in them, exits, is it outside)
from room_data import room_descriptions, room_articles, room_exits, room_outside, encounter_table, room_descriptions_winter, room_articles_winter
#import help topics for user
from help_file import help_topics
#import season and encounter class
from generation_classes import Season, Encounters
#import random module
import random

#This is a simple retro-style text based adventure game. You are an average human and you have a dog.
#Dogs need lots of exercise and time outside to do their business to remain healthy. You embark on a quest around the
#block in an effort to avoid a mess on the rug, and achieve an exercised pooch.

#While playing the game, you can 'look' to repeat the room information you are in, and notable objects can be examined
#with look <object>. There are commands you can send to achieve goals. You might get hints of these on the way.


#Fancy title.
print('')
print(' \    /\    / /\   |   | / ')
print('  \  /  \  / /__\  |   |<  ')
print('   \/    \/ /    \ |__ | \ ')
print('                   --|-- |  | |---')
print('                     |   |--| |---')
print('                     |   |  | |---')
print('                             |--\  ___  /--\ ')
print('                             |   ||   | | __')
print('                             |__/ |___| \__/')
print('')
print('                               Version 1.0')

#Ask for information to be used later, and store them each in a variable.
#Use a loop to return to asking questions if someone responds to the confirmation check below with
#either no or other words until he answer is yes. Use another while loop to check for answers that are not
#yes or no.

#Initialize the input variable.
confirm_input = ''

#Run loop until user inputs 'yes' at a specific point.
while confirm_input != 'yes':
    # Ask user what their dog's name and breed is.
    dog_breed = input('What breed is your dog? ')
    dog_name = input('What is your dog\'s name? ')

    #ask to confirm user choices
    print('So your dog is a %s, and its name is %s?' % (dog_breed, dog_name))

    #Internal while loop checks if confirm input is valid choice (yes or no)
    valid_input = False
    while not valid_input:
        confirm_input = input('Answer \'yes\' to continue, or \'no\' to restart: ')
        confirm_input = confirm_input.lower().strip()

        if confirm_input == 'yes':
            print('Your selections have been noted.')
            print('')
            valid_input = True
        elif confirm_input == 'no':
            print('Please input new answers.')
            print('')
            valid_input = True
        else:
            print('I did not understand that. Try again.')
            print('')
            valid_input = False

#We have some basic user data which will be used throughout the game.
#The program needs to set up some values to run properly.

#Set and init the parameters from the season class.
_season = Season("init_season", "init_temp", "init_weather")

#assign class random data to appropriate variables
current_season = _season.gen_season()
current_temp = _season.get_temp()
current_weather = _season.gen_weather()

#This was used to test the winter description switch
#current_season = 'winter'

#Set up encounters from encounter class
_encounter = Encounters(current_season, current_temp, current_weather, 1, 1, 1, 1)
_encounter.gen_enc_values()
stray_cats = _encounter.cats
stray_dogs = _encounter.strays
walking_dogs = _encounter.dog_walkers
walking_humans = _encounter.humans


#Initialize Load-in Room Data
#Load into your 'Bedroom' as the current_room
current_room = 'bedroom'
room_exit_list = 'Exits: '

#Print current room description for room you load into
print(room_descriptions[current_room])

#Get the room exits for your starting room and then print them. This is to allow for modular changes in the room_data
#dictionary, in case I want to add more exits later. Also add this returned value to a list for checking exits later
#as a part of initial set up of first room.
valid_exit = []

#load initial room exits into valid exit list from dictionary
for item, value in room_exits.items():
    for key in value:
        if item == current_room:
            room_exit_list = room_exit_list + ' ' + value[key].title()
            valid_exit.append(value[key].lower())

#load objects in the room into your initial room from dictionary
room_objects = []
key_grabber = ''
for item, value, in room_articles.items():
        for key in value:
            if item == current_room:
                key_grabber = key
                room_objects.append(key_grabber.lower())

#print the exits from initial room
print(room_exit_list)
print('')

#print initial data about the season/temperature
print('It is a {temp}, {season} day. The current weather is {weather}.'.format(temp=current_temp, season=current_season, weather=current_weather))

#load dog into a specified room without a leash on
dog_room = 'livingroom'
is_leashed = False

'''
#Randomly decide how long it will take for your dog to do his business, hopefully outside at the park. This value
#counts down as soon as you leave the front door the first time.
#Until then, dog object has a pee and a poo in his inventory.
rooms_to_poo = random.randint(10, 15)
rooms_to_pee = random.randint(5, 10)

FIXME: Removed due to time constraints on creating inventory system right now.
'''



#Use the generation variables to randomly scatter the entities in the world using encounter_table dictionary.
while stray_cats > 0:
    #pick a random dictionary key to use as spawn value
    spawn_room = random.choice(list(encounter_table.keys()))

    #Put spawn into encounter dictionary
    if encounter_table[spawn_room] == 'nothing':
        encounter_table[spawn_room] = 'cat'
    elif encounter_table[spawn_room] != 'nothing':
        #For simplicity, I don't want two entities in a room right now.
        #if an entity is already in the room, do nothing.
        continue

    #Deincrement number of cats to spawn
    stray_cats -= 1

while stray_dogs > 0:
    # pick a random dictionary key to use as spawn value
    spawn_room = random.choice(list(encounter_table.keys()))

    #Put spawn into encounter dictionary
    if encounter_table[spawn_room] == 'nothing':
        encounter_table[spawn_room] = 'stray'
    elif encounter_table[spawn_room] != 'nothing':
        # For simplicity, I don't want two entities in a room right now.
        # if an entity is already in the room, do nothing.
        continue

    #deincrement number of stray dogs to spawn
    stray_dogs -= 1

while walking_dogs > 0:
    # pick a random dictionary key to use as spawn value
    spawn_room = random.choice(list(encounter_table.keys()))

    # Put spawn into encounter dictionary
    if encounter_table[spawn_room] == 'nothing':
        encounter_table[spawn_room] = 'walkingdog'
    elif encounter_table[spawn_room] != 'nothing':
        # For simplicity, I don't want two entities in a room right now.
        # if an entity is already in the room, do nothing.
        continue

    #deincrement number of dogs walking with a human
    walking_dogs -= 1


while walking_humans > 0:
    # pick a random dictionary key to use as spawn value
    spawn_room = random.choice(list(encounter_table.keys()))

    # Put spawn into encounter dictionary
    if encounter_table[spawn_room] == 'nothing':
        encounter_table[spawn_room] = 'person'
    elif encounter_table[spawn_room] != 'nothing':
        # For simplicity, I don't want two entities in a room right now.
        # if an entity is already in the room, do nothing.
        continue

    #deincrement number of people to spawn
    walking_humans -= 1

#used for debugging random generation development
#print(encounter_table)


#The main loop that is the game. Loops until user types 'exit'.
while True:
    #Get user command inputs
    player_input = input('Your Action: ')
    print('')

    #lowercase, split into list, stripped of leading spaces if any
    player_input = player_input.lower().lstrip().split()

    #get the first word from the list, because its the command word
    command = player_input[0]
    #make 100% sure its lowercase (bug fix)
    command = command.lower()
    #clean up the list once you captured the command into 'command' variable
    del player_input[0]

    #any words following are args in the list used as modifiers to a command.
    #put them into command_args
    command_args = ''
    for item in player_input:
        command_args = command_args + ' ' + item

    #make sure they're stripped of leading whitespace and lower case
    command_args = command_args.lstrip().lower()

    #Look Command
    #if it has no arg, print current room description and exits
    if command == 'look' and command_args == '':

        is_outside = room_outside[current_room]

        if (current_season != 'winter') or (is_outside == False):
            print(room_descriptions[current_room])
        elif (current_season == 'winter') and (is_outside == True):
            print(room_descriptions_winter[current_room])
        print(room_exit_list)
        print('')

        #if dog is in this room, print extra line to tell you the dog is here.
        if dog_room == current_room:
            print('%s the %s dog is here.' % (dog_name.title(), dog_breed.title()))
            print('')

        #Only worry about printing encounters if room is outside.
        #if an encounter matches room in dictionary table, print that it exists there.
        if is_outside == True:
            if encounter_table[current_room] != 'nothing':
                if encounter_table[current_room] == 'cat':
                    print('There is a stray cat here.')
                elif encounter_table[current_room] == 'stray':
                    print('There is a stray dog sniffing around.')
                elif encounter_table[current_room] == 'walkingdog':
                    print('A person is walking with their dog.')
                elif encounter_table[current_room] == 'human':
                    print('There is a person here, going about their day.')
            print('It is a {temp}, {season} day. The current weather is {weather}.'.format(temp=current_temp, season=current_season, weather=current_weather))

    #if look has an argument found, check if its a room object and print description of it.
    elif command == 'look' and command_args != '':
        #Season check, because descriptions change seasonally.

        #only worry about winter descriptions in outside rooms
        if (current_season == 'winter') and (is_outside == True):
            if command_args in room_objects:
                for item, value in room_articles_winter.items():
                    for key in value:
                        #if its a valid object in the room, get info from dictionary
                        if key == command_args and item == current_room:
                            print(value[key])
                            print('')
        # if it isn't winter or outside, proceed as usual.
        elif (current_season != 'winter') or (is_outside == False):
            if command_args in room_objects:
                for item, value in room_articles.items():
                    for key in value:
                        #if its a valid object in the room, get info from dictionary
                        if key == command_args and item == current_room:
                            print(value[key])
                            print('')
        #if dog is here and you look at it, print info about dog
        elif (command_args == 'dog') or (command_args == dog_name):
            if dog_room == current_room:
                print('A four legged furry companion animal that you call %s.' % dog_name.title())
                print('')

        #is there an encounter here?
        elif command_args == encounter_table[current_room]:
            if encounter_table[current_room] == 'cat':
                print('A small, fickle furry animal roaming the neighborhood.')
            elif encounter_table[current_room] == 'stray':
                print('Someone\'s dog seems to have escaped the yard.')
            elif encounter_table[current_room] == 'walkingdog':
                print('A person is outside walking their dog.')
            elif encounter_table[current_room] == 'human':
                print('This individual is going about their day.')
        #if nothing is valid for provided arg, tell user 'you dont see that.'
        else:
            print('You don\'t see anything like that here.')
            print('')

    #Check for valid exits. If match to user input and is a valid exit for that room - move to that room.
    elif command in valid_exit:

        #set current room to new room
        once = 1
        for item, value in room_exits.items():
            for key in value:
                if value[key] == command and item == current_room and once == 1:
                    once = 2
                    current_room = key

        #set up the exit list from the new room
        room_exit_list = 'Exit: '
        valid_exit = []

        #get valid exits for new room stored
        for item, value in room_exits.items():
            for key in value:
                if item == current_room:
                    room_exit_list = room_exit_list + ' ' + value[key].title()
                    valid_exit.append(value[key].lower())

        #grab and set up the list of objects in the new room
        room_objects = []
        key_grabber = ''

        is_outside = room_outside[current_room]
        #Winter changes descriptions. Grab descriptions from winter item list.
        if (current_season == 'winter') and (is_outside == True):
            for item, value, in room_articles_winter.items():
                for key in value:
                    if item == current_room:
                        key_grabber = key
                        room_objects.append(key_grabber.lower())
        #if not winter or inside, proceed as normal.
        else:
            for item, value, in room_articles.items():
                for key in value:
                    if item == current_room:
                        key_grabber = key
                        room_objects.append(key_grabber.lower())

        #debug - what is the current room id?
        #print('current room id is', current_room)

        #If your dog is leashed, it needs to come with you when you move to the new room.
        if is_leashed == True:
            print('%s the %s dog follows you on its leash.' % (dog_name.title(), dog_breed.title()))
            print('')
            dog_room = current_room

        #print the new room.
        #print winter descriptions if outside and season is winter.
        if (current_season == 'winter') and (is_outside == True):
            print(room_descriptions_winter[current_room])
        #if not outside or winter proceed as usual.
        else:
            print(room_descriptions[current_room])

        print(room_exit_list)
        print('')


        #if an entity spawned in the room, print it as being here.
        #they only happen in a room that is 'outside'.
        is_outside = room_outside[current_room]

        if is_outside == True:
            if encounter_table[current_room] != 'nothing':
                if encounter_table[current_room] == 'cat':
                    print('There is a stray cat here.')
                elif encounter_table[current_room] == 'stray':
                    print('There is a stray dog sniffing around.')
                elif encounter_table[current_room] == 'walkingdog':
                    print('A person is walking with their dog.')
                elif encounter_table[current_room] == 'human':
                    print('There is a person here, going about their day.')
            print('It is a {temp}, {season} day. The current weather is {weather}.'.format(temp=current_temp, season=current_season, weather=current_weather))

        #if your dog is in this room as you move in print that too.
        if dog_room == current_room:
            print('%s the %s dog is here.' % (dog_name.title(), dog_breed.title()))
            print('')

    #Leash command
    #If no arg, ask what to put the leash on
    elif command == 'leash' and command_args == '':
        print('Leash what?')
        print('')

    #Check for 'dog' as arg
    #if dog already has leash on, say it is already leashed
    elif command == 'leash' and command_args == 'dog' or command_args == dog_name:
        if dog_room == current_room:
            if is_leashed == True:
                print('But %s is already clipped onto your leash.' % dog_name.title())
            else:
                #if dog is not already leashed, put leash on.
                is_leashed = True
                print('You clip a leash to %s the %s. It now follows you.' % (dog_name.title(), dog_breed.title()))
                print('')

    #Remove leash with 'off' as arg to leash command
    #check for no leash
    elif command == 'leash' and command_args == 'off':
        if is_leashed == False:
            print('You fail to remove the leash as %s isn\'t clipped onto your leash already.' % dog_name.title())
            print('')
        else:
            #if you are outside the house, you cannot take the leash off.
            is_outside = room_outside[current_room]
            if is_outside == True:
                print('Due to local bylaws, all dogs must be on a leash outside. Return home to remove it.')
                print('')
            else:
                #Take the leash off.
                is_leashed = False
                print('You un-clip the leash from %s. He no longer follows you.' % dog_name.title())
                print('')

    #Help command
    #print help topics from a dictionary
    elif command == 'help':
        print('Printing help topics...')
        for item, value in help_topics.items():
            print(item + ': ' + value)
        print('')

    #exit command - exits the program
    elif command == 'exit':
        print('Exiting...')
        break

    #if not a valid command, tell user.
    else:
        print('Invalid command. Type \'help\' for help topics.')

