__author__ = 'Victoria King'

from room_data import room_descriptions, room_articles, room_exits, room_outside
from help_file import help_topics

#This is a simple retro-style text based adventure game. You are an average human and you have a dog.
#Dogs need lots of exercise and time outside to do their business to remain healthy. You embark on a quest around the
#block in an effort to avoid a mess on the rug, and achieve an exercised pooch.

#While playing the game, you can 'look' to repeat the room information you are in, and notable objects can be examined
#with look <object>. There are commands you can send to achieve goals. You might get hints of these on the way.


#Fancy title.
print ""
print " \    /\    / /\   |   | / "
print "  \  /  \  / /__\  |   |<  "
print "   \/    \/ /    \ |__ | \ "
print "                   --|-- |  | |---"
print "                     |   |--| |---"
print "                     |   |  | |---"
print "                             |--\  ___  /--\ "
print "                             |   ||   | | __"
print "                             |__/ |___| \__/"
print ""
print "                               Version 1.0"

#Ask for information to be used later, and store them each in a variable.
#Use a loop to return to asking questions if someone responds to the confirmation check below with
#either no or other words until he answer is yes. Use another while loop to check for answers that are not
#yes or no.

confirm_input = ""


while confirm_input != "yes":
    dog_breed = raw_input("What breed is your dog? ")
    dog_name = raw_input("What is your dog's name? ")

    print "So your our dog is a %s, and its name is %s?" % (dog_breed, dog_name)

    valid_input = False
    while not valid_input:
        confirm_input = raw_input("Answer 'yes' to continue, or 'no' to restart: ")
        confirm_input = confirm_input.lower().strip()

        if confirm_input == "yes":
            print "Your selections have been noted."
            print ""
            valid_input = True
        elif confirm_input == "no":
            print "Please input new answers."
            print ""
            valid_input = True
        else:
            print "I didn't understand that. Try again."
            print ""
            valid_input = False

#We have some basic user data which will be used throughout the game now. The program needs to set up some values now.

#Initialize Load-in Room Data - Load into your Bedroom
current_room = "bedroom"
room_exit_list = "Exits: "

#Print Bedroom description
print room_descriptions[current_room]

#Get the room exits for your bedroom and then print them. This is to allow for modular changes in the room_data
#dictionary, in case I want to add more exits later. Also add this returned value to a list for checking exits later
#as a part of initial set up of first room.
valid_exit = []

for item, value in room_exits.items():
    for key in value:
        if item == current_room:
            room_exit_list = room_exit_list + " " + value[key].title()
            valid_exit.append(value[key].lower())

room_objects = []
key_grabber = ""
for item, value, in room_articles.items():
    for key in value:
        if item == current_room:
            key_grabber = key
            room_objects.append(key_grabber.lower())

print room_exit_list
print ""

dog_room = "livingroom"
is_leashed = False

#The main loop that is the game's functionality.
while True:
    player_input = raw_input("Your Action: ")
    print ""

    player_input = player_input.lower().lstrip().split()

    command = player_input[0]
    command = command.lower()
    del player_input[0]

    command_args = ""
    for item in player_input:
        command_args = command_args + " " + item

    command_args = command_args.lstrip().lower()

    #Look Command
    if command == "look" and command_args == "":
        print room_descriptions[current_room]
        print room_exit_list
        print ""
        if dog_room == current_room:
            print "%s the %s dog is here." % (dog_name.title(), dog_breed.title())
            print ""

    #if look has an argument found, check if its a room object and print description of it.
    elif command == "look" and command_args != "":
        if command_args in room_objects:
            for item, value in room_articles.items():
                for key in value:
                    if key == command_args and item == current_room:
                        print value[key]
                        print ""
        elif command_args == "dog" or command_args == dog_name:
            if dog_room == current_room:
                print "A four legged furry companion animal that you call %s." % dog_name.title()
                print ""
        else:
            print "You don't see anything like that here."
            print ""

    #Check for valid exits. If match to command - move to that room.
    elif command in valid_exit:

        #set current room to new room
        once = 1
        for item, value in room_exits.items():
            for key in value:
                if value[key] == command and item == current_room and once == 1:
                    once = 2
                    current_room = key

        #set up the exit list from the new room
        room_exit_list = "Exit: "
        valid_exit = []

        for item, value in room_exits.items():
            for key in value:
                if item == current_room:
                    room_exit_list = room_exit_list + " " + value[key].title()
                    valid_exit.append(value[key].lower())

        #grab and set up the list of objects in the new room
        room_objects = []
        key_grabber = ""
        for item, value, in room_articles.items():
            for key in value:
                if item == current_room:
                    key_grabber = key
                    room_objects.append(key_grabber.lower())

        #If your dog is leashed, it needs to come with you.
        if is_leashed == True:
            print "%s the %s dog follows you on its leash." % (dog_name.title(), dog_breed.title())
            print ""
            dog_room = current_room

        #print the new room.
        print room_descriptions[current_room]
        print room_exit_list
        print ""

        #if your dog is in this room as you move in print that too.
        if dog_room == current_room:
            print "%s the %s dog is here." % (dog_name.title(), dog_breed.title())
            print ""

    elif command == "leash" and command_args == "":
        print "Leash what?"
        print ""

    elif command == "leash" and command_args == "dog" or command_args == dog_name:
        if dog_room == current_room:
            if is_leashed == True:
                print "But %s is already clipped onto your leash." % dog_name.title()
            else:
                is_leashed = True
                print "You clip a leash to %s the %s. It now follows you." % (dog_name.title(), dog_breed.title())
                print ""

    elif command == "leash" and command_args == "off":
        if is_leashed == False:
            print "You fail to remove the leash as %s isn't clipped onto your leash already." % dog_name.title()
            print ""
        else:
            is_outside = room_outside[current_room]
            if is_outside == True:
                print "Due to local bylaws, all dogs must be on a leash outside. Return home to remove it."
                print ""
            else:
                is_leashed = False
                print "You un-clip the leash from %s. He no longer follows you." % dog_name.title()
                print ""

    elif command == "help":
        print "Printing help topics..."
        for item, value in help_topics.items():
            print item + ": " + value
        print ""

    elif command == "exit":
        print "Exiting..."
        break

    else:
        print "Invalid command. Type 'help' for help topics."

#In a future update, Seasons, and inventory will come into play. Encounters will follow.