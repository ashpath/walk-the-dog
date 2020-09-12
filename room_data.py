__author__ = 'Victoria'

#Data about the main descriptions of rooms.
room_descriptions = {
    'bedroom': 'This is your bedroom. There is a bed, a nightstand, and a window with some curtains.',
    'closet': 'This is some sort of walk-in closet. Clothes hang on rails and shoes sit on the floor. It '
              'seems like there is a hatch above you that goes to the attic.',
    'hall1':  'This is a hallway. There is a window and a carpet here. It continues south. Your bedroom is west.',
    'hall2': 'This is a hallway. There is a carpet here, covering the floor. There is a room to the west.',
    'hall3': 'This is a hallway. There is a carpet and a window here. Some stairs lead down.',
    'bathroom1': 'This is a bathroom. There is a bathtub, a sink, a toilet and a shower head here.',
    'office': 'This is your home office. You see a desk with a computer on it, some shelves, and motivational posters '
              'line the walls.',
    'entryway': 'A high traffic area in your house. The stairway here goes upstairs, a front door goes outside, a door '
                'to the west leads to a small bathroom, while to the north is a hallway.',
    'bathroom2': 'A tiny little cubicle of a bathroom. Unlike the one upstairs, this one does not have a shower or a '
                 'bathtub present. There is only a toilet and a sink for doing your business while on the lower level.',
    'hall4': 'You are standing in a hallway. Your living room is to the west. A kitchen is northward. There isn\'t '
             'much here to look at.',
    'livingroom': 'You are in a living room. There is a fireplace, some furniture, and a large panel TV mounted on the '
                  'wall. The hardwood floor has been replaced with white carpet for comfort in this room.',
    'diningroom': 'This is a dining room. A big table with four chairs sits here, waiting for people to eat with.',
    'kitchen': 'This is your kitchen. There is a range and a sink here. A trashcan sits in a corner. Several appliances'
               ' sit upon the counters, and cabinets here probably hold more things.',
    'porch': 'You are outside on your front porch. A flowerpot sits here. To the northeast, your grassy yard '
             'continues, bordered by a fence. The fence gate is to the south.',
    'yard1': 'A small grassy yard with a large tree. Your house is on one side, and a fence on the other. It continues '
             'north.',
    'yard2': 'A small grassy yard. A rusty push mower is parked in front of a shed. A back gate leads east. The yard '
             'continues to the south.',
    'yard3': 'A simple grassy yard with a fence bordering the southern and eastern sides. The yard continues north. '
             'Your porch is to the west. Some patio furniture sits here.',
    'road1': 'You are on a sidewalk next to a road. To the north is the fence bordering your yard, with a gate leading '
             'into it.',
    'road2': 'You are at a corner on a sidewalk. To the north is the fence bordering your yard.',
    'road3': 'You are on a sidewalk next to a road. To the west is the fence bordering your yard.',
    'road4': 'You are on a sidewalk next to a road. To the west is the fence bordering your yard. You see a large tree'
             ' jutting from the yard behind the fence to the west.',
    'road5': 'You are on a sidewalk next to a road. To the west is the fence bordering your yard, with a gate leading '
             'into it.',
    'road6': 'You are on a sidewalk next to a road. To the north, the park behind your house is visible.',
    'road7': 'You are on a sidewalk at a street corner. Across the street to the north lies the park.',
    'park1': 'You are at the center of the park. There is a fountain with a large statue of a lion on a rock in the '
             'middle of the fountain, a stream of water flowing from its mouth. You are surrounded by flower beds '
             'that occupy all the space that the walkways do not.',
    'park2': 'You are at the northern side of the park. Flowerbeds occupy all the space that the walkways do not. '
             'There is a trashcan here. Pigeons strut around the trashcan, pecking for scraps.',
    'park3': 'You are at the northeastern side of the park. Flowerbeds occupy all the space that the walkways do not. '
             'There is a lamppost here, for illuminating the walkways at night.',
    'park4': 'You are at the eastern side of the park. Flowerbeds occupy all the space that the walkways do not. '
             'There is a bench for people to sit on here. Pigeons hop around the ground, looking for scraps.',
    'park5': 'You are at the southeastern side of the park. Flowerbeds occupy all the space that the walkways do not. '
             'There is a lamppost here, for illuminating the walkways at night.',
    'park6': 'You are at the southern side of the park. Flowerbeds occupy all the space that the walkways do not. '
             'There is a trashcan here.',
    'park7': 'You are at the southwestern side of the park. Flowerbeds occupy all the space that the walkways do not. '
             'There is a lamppost here, for illuminating the walkways at night.',
    'park8': 'You are at the western side of the park. Flowerbeds occupy all the space that the walkways do not. '
             'There is a bench for people to sit on here.',
    'park9': 'You are at the northwestern side of the park. Flowerbeds occupy all the space that the walkways do not. '
             'There is a lamppost here, for illuminating the walkways at night.',
}

#Data about room exits.
room_exits = {
    'bedroom': {
        'hall1': 'east',
        'closet': 'west',
    },
    'closet': {
        'bedroom': 'east',
    },
    'hall1': {
        'bedroom': 'west',
        'hall2': 'south',
    },
    'hall2': {
        'hall1': 'north',
        'hall3': 'south',
        'bathroom1': 'west',
    },
    'hall3': {
        'hall2': 'north',
        'office': 'west',
        'entryway': 'down',
    },
    'bathroom1': {
        'hall2': 'east',
    },
    'office': {
        'hall3': 'east',
    },
    'entryway': {
        'hall3': 'up',
        'bathroom2': 'west',
        'porch': 'south',
        'hall4': 'north',
    },
    'bathroom2': {
        'entryway': 'east',
    },
    'hall4': {
        'entryway': 'south',
        'livingroom': 'west',
        'kitchen': 'north',
    },
    'livingroom': {
        'hall4': 'east',
        'diningroom': 'north',
    },
    'diningroom': {
        'livingroom': 'south',
        'kitchen': 'east',
    },
    'kitchen': {
        'diningroom': 'west',
        'hall4': 'south',
    },
    'porch': {
        'yard1': 'northeast',
        'yard3': 'east',
        'road1': 'south',
    },
    'yard1': {
        'porch': 'southwest',
        'yard2': 'north',
        'yard3': 'south',
    },
    'yard2': {
        'yard1': 'south',
        'road5': 'east',
    },
    'yard3': {
        'yard1': 'north',
        'porch': 'west',
    },
    'road1': {
        'porch': 'north',
        'road2': 'east',
    },
    'road2': {
        'road1': 'west',
        'road3': 'northeast',
    },
    'road3': {
        'road2': 'southwest',
        'road4': 'north',
    },
    'road4': {
        'road3': 'south',
        'road5': 'north',
    },
    'road5': {
        'road4': 'south',
        'yard2': 'west',
        'road6': 'north',
    },
    'road6': {
        'road5': 'south',
        'road7': 'north',
    },
    'road7': {
        'road6': 'south',
        'park6': 'north',
    },
    'park1': {
        'park2': 'north',
        'park3': 'northeast',
        'park4': 'east',
        'park5': 'southeast',
        'park6': 'south',
        'park7': 'southwest',
        'park8': 'west',
        'park9': 'northwest',
    },
    'park2': {
        'park1': 'south',
        'park3': 'east',
        'park9': 'west',
    },
    'park3': {
        'park2': 'west',
        'park4': 'south',
        'park1': 'southwest',
    },
    'park4': {
        'park1': 'west',
        'park3': 'north',
        'park5': 'south',
    },
    'park5': {
        'park1': 'northwest',
        'park4': 'north',
        'park6': 'west',
    },
    'park6': {
        'park1': 'north',
        'park5': 'east',
        'park7': 'west',
    },
    'park7': {
        'park1': 'northeast',
        'park6': 'east',
        'park8': 'north',
    },
    'park8': {
        'park1': 'east',
        'park7': 'south',
        'park9': 'north',
    },
    'park9': {
        'park1': 'southeast',
        'park8': 'south',
        'park2': 'east',
    },
}

#Data about objects you can see in rooms.
room_articles = {
    'bedroom': {
        'bed': 'Its your bed, and its pretty comfy. It has to be, you use it every night.',
        'nightstand': 'A small bedside furniture piece. A book, a lamp, and a clock sit upon it.',
        'book': 'The book is titled \'Fifty Shades of Blue and Yellow: How Dogs See the World\'.',
        'lamp': 'It isn\'t the prettiest lamp, but its functional.',
        'window': 'The window has been jammed shut since before you lived here. It cannot be opened.',
        'curtains': 'Wow, these are ugly. Note to self: replace these.',
        'walls': 'Simple eggshell white colored walls. A poster of your favorite game is hung on one of them.',
        'poster': 'A gift from a friend who understands how much you love this game.',
        'clock': 'It tells the time, plays the radio, and wakes you up in the morning.',
        'floor': 'A simple hardwood floor. Easy to clean, but cold on bare feet.'
    },
    'closet': {
        'shoes': 'These are some fancy shoes for special occasions. Not ideal for regular outside usage.',
        'clothes': 'These clothes hang on various implements. A few pieces of clothing have sat unworn for some time.',
        'hatch': 'This lets you go up to the attic. You don\'t really want to go up there right now, its all '
                 'spiderwebs and junk.',
        'walls': 'There is so much junk in the closet that you cannot see the walls.',
        'floor': 'Between piles of stuff on the floor, you note that it is a simple hardwood floor.'
    },
    'hall1': {
        'window': 'The window allows light in, but is a single pane and has no mechanism to be opened.',
        'carpet': 'A simple plushy carpet that feels pretty good on bare feet.',
        'walls': 'Simple eggshell white colored walls.',
        'floor': 'A carpet is covering the hardwood the floor is made of.'
    },
    'hall2': {
        'carpet': 'A simple plushy carpet that feels pretty good on bare feet.',
        'walls': 'Simple eggshell white colored walls.',
        'floor': 'A carpet is covering the hardwood the floor is made of.'
    },
    'hall3': {
        'window': 'The window allows light in, but is a single pane and has no mechanism to be opened.',
        'carpet': 'A simple plushy carpet that feels pretty good on bare feet.',
        'walls': 'Simple eggshell white colored walls. A poster of your favorite game is hung on one of them.',
        'stairs': 'Covered in white carpet with a metal railing, they lead downstairs.',
        'floor': 'A carpet is covering the hardwood the floor is made of.'
    },
    'bathroom1': {
        'sink': 'One of many common bathroom items, it dispenses and holds liquid water.',
        'tub': 'A common bathroom article designed to hold a large volume of water.',
        'bathtub': 'A common bathroom article designed to hold a large volume of water.',
        'showerhead': 'Sprouting from the wall over the bathtub, this implement spews liquid water.',
        'toilet': 'A device used as needed for defecating.',
        'walls': 'The upper half of the wall is a sort of steel-blue. The lower half is covered in marble tiles.',
        'floor': 'The floor here is covered in smooth marble tiles.'
    },
    'office': {
        'desk': 'Something to put your computer on. It ends up looking more like a recycling bin though with all the '
                'paper sitting on it.',
        'paper': 'You really should get a filing cabinet or something for those.',
        'computer': 'While it can be used for important things, you find yourself inevitably looking at piles of cat '
                    'photographs from the internet.',
        'shelf': 'There is more than one shelf in here.',
        'shelves': 'A generic dumping ground for books and knick-knacks until you need them again.',
        'posters': 'Hang in there! Teamwork! We can do this! Pick up eggs, milk, butter... oh wait, that\'s a grocery '
                   'list on a stick-it note.',
        'floor': 'A simple hardwood floor. Easy to clean, but cold on bare feet.',
        'walls': 'Covered in motivational posters.'
    },
    'entryway': {
        'door': 'A heavy oak door serves as an entry and exit from your home. It leads outside to your porch.',
        'stairs': 'These stairs have been covered in white carpet and are accompanied upstairs by a metal railing.',
        'floor': 'The floor here is made of hardwood. It ends at the stairs, replaced by white carpet.',
        'walls': 'Simple eggshell white colored walls.'
    },
    'bathroom2': {
        'sink': 'One of many common bathroom items, it dispenses and holds liquid water.',
        'toilet': 'A device used as needed for defecating.',
        'walls': 'The walls here are some sort of gray-green. A tiny framed picture hangs on a wall.',
        'picture': 'Its an abstract painting composed of several brush strokes. You have no idea who painted it.',
        'floor': 'A simple hardwood floor. Easy to clean, but cold on bare feet.',
    },
    'hall4': {
        'walls': 'Simple eggshell white colored walls.',
        'floor': 'A simple hardwood floor. Easy to clean, but cold on bare feet.'
    },
    'livingroom': {
        'walls': 'Simple eggshell white colored walls.',
        'floor': 'Luxuriously plushy white carpet that feels pretty good on bare feet.',
        'fireplace': 'A place to light firewood. Usually used during the winter.',
        'furniture': 'You see a couch, a recliner, and a coffee table.',
        'couch': 'A big leather couch. It seems to be a singularity for people, as those that pass the \'couch event'
                 ' horizon\' never seem to be able to get up again. It\'s really that comfortable.',
        'recliner': 'For those extremely lazy days where getting stuck in the \'black hole\' couch just won\'t do for '
                    'you.',
        'table': 'A little knee-high table for putting newspapers, magazines, coasters and drinks onto.',
        'coffee table': 'A little knee-high table for putting newspapers, magazines, coasters and drinks onto.',
        'tv': 'You wish it was an organic LED TV, but are well aware that OLED also means \'only Lawyers, Executives, '
              'and Doctors\' based on the price tags.'
    },
    'diningroom': {
        'table': 'A large wooden table spans the room. Its about the right size to host a family feast.',
        'chairs': 'Four chairs sit pushed in at the table. They are simple chairs made of wood.',
        'walls': 'Simple eggshell white colored walls.',
        'floor': 'A simple hardwood floor. Easy to clean, but cold on bare feet.'
    },
    'kitchen': {
        'walls': 'Simple eggshell white colored walls.',
        'floor': 'Some sort of linoleum. Its easy to clean spills off of.',
        'counter': 'The counters are made of black granite.',
        'range': 'A large appliance. You can set pots on top of it to cook, or use the oven to bake with.',
        'sink': 'A large stainless steel kitchen sink. You usually use it to wash the dishes, because you have no space'
                ' for a dishwasher.',
        'appliances': 'You see: A Toaster, a Blender, a Microwave, and a Coffee Maker.',
        'toaster': 'Directions: Insert bread. Wait. Receive toast. Proceed to burn fingertips.',
        'blender': 'This appliance turns most things inserted within into a mass of goo. Sometimes it\'s delicious '
                   'goo, based on the ingredients.',
        'microwave': 'Because using pots and pans is too much work sometimes.',
        'coffee maker': 'A machine that takes water and coffee grounds as input, and outputs liquid insomnia.',
        'trashcan': 'Phew, that stinks. You may want to consider taking this outside soon.',
        'cabinets': 'They\'re really just big junk and tableware holders.',
        'coffee': 'Oh. That\'s where you left it.',
        'sandwich': 'Delicious.'
    },
    'porch': {
        'grass': 'A ground covering plant, its green in color and needs to be mowed soon.',
        'fence': 'A standard fence. Its been stained a natural color rather than painted.',
        'flowerpot': 'A large pot filled with various small flowers, for decoration.',
        'gate': 'A simple fence gate leads out.'
    },
    'yard1': {
        'grass': 'A ground covering plant, its green in color and needs to be mowed soon.',
        'fence': 'A standard fence. Its been stained a natural color rather than painted.',
        'tree': 'A large cherry tree, typical of this area. It blooms a beautiful pink in spring.',
        'house': 'Not the largest house on the block, but its a place to live.'
    },
    'yard2': {
        'grass': 'A ground covering plant, its green in color and needs to be mowed soon.',
        'fence': 'A standard fence. Its been stained a natural color rather than painted.',
        'mower': 'This push mower has seen better days. Its completely rusted out and unusable.',
        'push mower': 'This push mower has seen better days. Its completely rusted out and unusable.',
        'shed': 'A place where you put your tools and spiders set up face traps for you to walk into. You don\'t '
                'feel like getting webbed today, so let\'s not go in there unless we have to.',
        'gate': 'A simple fence gate leads out.'
    },
    'yard3': {
        'grass': 'A ground covering plant, its green in color and needs to be mowed soon.',
        'fence': 'A standard fence. Its been stained a natural color rather than painted.',
        'furniture': 'Stackable plastic outdoor furniture.'
    },
    'road1': {
        'gate': 'A simple fence gate leads inward.',
        'fence': 'A standard fence. Its been stained a natural color rather than painted.',
        'sidewalk': 'A concrete road bordering a road, designed for pedestrian traffic.',
        'road': 'An asphalt road designed for vehicles to drive on.'
    },
    'road2': {
        'fence': 'A standard fence. Its been stained a natural color rather than painted.',
        'sidewalk': 'A concrete road bordering a road, designed for pedestrian traffic.',
        'road': 'An asphalt road designed for vehicles to drive on.'
    },
    'road3': {
        'fence': 'A standard fence. Its been stained a natural color rather than painted.',
        'sidewalk': 'A concrete road bordering a road, designed for pedestrian traffic.',
        'road': 'An asphalt road designed for vehicles to drive on.'
    },
    'road4': {
        'fence': 'A standard fence. Its been stained a natural color rather than painted.',
        'sidewalk': 'A concrete road bordering a road, designed for pedestrian traffic.',
        'road': 'An asphalt road designed for vehicles to drive on.',
        'tree': 'A large cherry tree, typical of this area. It blooms a beautiful pink in spring.'
    },
    'road5': {
        'fence': 'A standard fence. Its been stained a natural color rather than painted.',
        'sidewalk': 'A concrete road bordering a road, designed for pedestrian traffic.',
        'road': 'An asphalt road designed for vehicles to drive on.',
        'gate': 'A simple fence gate leads inward.'
    },
    'road6': {
        'fence': 'A standard fence. Its been stained a natural color rather than painted.',
        'sidewalk': 'A concrete road bordering a road, designed for pedestrian traffic.',
        'road': 'An asphalt road designed for vehicles to drive on.',
        'park': 'It isn\'t a huge park, but you enjoy using this green space nonetheless.'
    },
    'road7': {
        'fence': 'A standard fence. Its been stained a natural color rather than painted.',
        'sidewalk': 'A concrete road bordering a road, designed for pedestrian traffic.',
        'road': 'An asphalt road designed for vehicles to drive on.',
        'park': 'It\'s right across the street. People flock here to walk around in it.'
    },
    'park1': {
        'fountain': 'A large fountain at the center of the park. People seem to throw a lot of change in based on '
                    'a superstition of good luck.',
        'statue': 'A large lion is sitting on a rocky island in the middle of the fountain. A gentle stream of water '
                  'spews out of the lion\'s mouth.',
        'lion': 'A large lion is sitting on a rocky island in the middle of the fountain. A gentle stream of water '
                  'spews out of the lion\'s mouth.',
        'flowers': 'There are so many flowers you cannot even dream of trying to count them in a timely manner.',
        'flower beds': 'The spaces between the paved walkways are filled with flowers.',
        'walkway': 'A paved concrete sidewalk for pedestrians that leads you around the park.'
    },
    'park2': {
        'flowers': 'There are so many flowers you cannot even dream of trying to count them in a timely manner.',
        'flower beds': 'The spaces between the paved walkways are filled with flowers.',
        'walkway': 'A paved concrete sidewalk for pedestrians that leads you around the park.',
        'trashcan': 'This particular trashcan is stuffed full beyond capacity. Some of its contents have spilled '
                    'onto the ground.',
        'pigeons': 'These \'flying rats\' are here scavenging food from the overstuffed trashcan.'
    },
    'park3': {
        'flowers': 'There are so many flowers you cannot even dream of trying to count them in a timely manner.',
        'flower beds': 'The spaces between the paved walkways are filled with flowers.',
        'walkway': 'A paved concrete sidewalk for pedestrians that leads you around the park.',
        'lamppost': 'A tall lamppost with a flower pot hung from a hook on the post.'
    },
    'park4': {
        'flowers': 'There are so many flowers you cannot even dream of trying to count them in a timely manner.',
        'flower beds': 'The spaces between the paved walkways are filled with flowers.',
        'walkway': 'A paved concrete sidewalk for pedestrians that leads you around the park.',
        'bench': 'A place to sit. This bench is infested with a flock of Pigeons, and covered in droppings. Not '
                 'the nicest place to sit currently, on second thought.',
        'pigeons': 'These \'flying rats\' are here doing pigeon things and making a mess on the bench.'
    },
    'park5': {
        'flowers': 'There are so many flowers you cannot even dream of trying to count them in a timely manner.',
        'flower beds': 'The spaces between the paved walkways are filled with flowers.',
        'walkway': 'A paved concrete sidewalk for pedestrians that leads you around the park.',
        'lamppost': 'A tall lamppost with a flower pot hung from a hook on the post.'
    },
    'park6': {
        'flowers': 'There are so many flowers you cannot even dream of trying to count them in a timely manner.',
        'flower beds': 'The spaces between the paved walkways are filled with flowers.',
        'walkway': 'A paved concrete sidewalk for pedestrians that leads you around the park.',
        'trashcan': 'This particular trashcan looks like it still has some room left inside.'
    },
    'park7': {
        'flowers': 'There are so many flowers you cannot even dream of trying to count them in a timely manner.',
        'flower beds': 'The spaces between the paved walkways are filled with flowers.',
        'walkway': 'A paved concrete sidewalk for pedestrians that leads you around the park.',
        'lamppost': 'A tall lamppost with a flower pot hung from a hook on the post.'
    },
    'park8': {
        'flowers': 'There are so many flowers you cannot even dream of trying to count them in a timely manner.',
        'flower beds': 'The spaces between the paved walkways are filled with flowers.',
        'walkway': 'A paved concrete sidewalk for pedestrians that leads you around the park.',
        'bench': 'A place to sit. This bench is located in a nice quiet side of the park. It is the bench of '
                 'choice for anyone wanting a sit in the park.'
    },
    'park9': {
        'flowers': 'There are so many flowers you cannot even dream of trying to count them in a timely manner.',
        'flower beds': 'The spaces between the paved walkways are filled with flowers.',
        'walkway': 'A paved concrete sidewalk for pedestrians that leads you around the park.',
        'lamppost': 'A tall lamppost with a flower pot hung from a hook on the post.'
    },
}

#change outdoor room descriptions in winter
room_descriptions_winter = {
    'porch': 'You are outside on your front porch. An empty flowerpot sits here. To the northeast, your snowy yard '
             'continues, bordered by a fence. The fence gate is to the south.',
    'yard1': 'A small snow covered yard with a large tree. Your house is on one side, and a fence on the other. '
             'It continues north.',
    'yard2': 'A small snow covered yard. A rusty push mower is parked in front of a shed. A back gate leads east. '
             'The yard continues to the south.',
    'yard3': 'A simple snowy yard with a fence bordering the southern and eastern sides. The yard continues north. '
             'Your porch is to the west. Some patio furniture sits here.',
    'road1': 'You are on a snowy sidewalk next to a road. To the north is the fence bordering your yard, '
             'with a gate leading into it.',
    'road2': 'You are at a corner on a sidewalk. Everything is covered in snow and ice. '
             'To the north is the fence bordering your yard.',
    'road3': 'You are on a sidewalk next to a road. Everything is covered in snow and ice. '
             'To the west is the fence bordering your yard.',
    'road4': 'You are on a sidewalk next to a road. Everything is covered in snow and ice. To the west is the fence '
             'bordering your yard. You see a large tree jutting from the yard behind the fence to the west.',
    'road5': 'You are on a sidewalk next to a road. Everything is covered in snow and ice. '
             'To the west is the fence bordering your yard, with a gate leading into it.',
    'road6': 'You are on a sidewalk next to a road. Everything is covered in snow and ice. '
             'To the north, the park behind your house is visible.',
    'road7': 'You are on a sidewalk at a street corner. Everything is covered in snow and ice. '
             'Across the street to the north lies the park.',
    'park1': 'You are at the center of the park. Everything is covered in snow and ice. '
             'There is a frozen fountain with a large statue of a lion on a rock in the '
             'middle of the fountain. There would normally be flowers, but they are covered by snow.',
    'park2': 'You are at the northern side of the park. Everything is covered in snow and ice. '
             'There would normally be flowers, but they are covered by snow. '
             'There is a trashcan here. Pigeons strut around the trashcan, pecking for scraps.',
    'park3': 'You are at the northeastern side of the park. Everything is covered in snow and ice. '
             'There would normally be flowers, but they are covered by snow. '
             'There is a lamppost here, for illuminating the walkways at night.',
    'park4': 'You are at the eastern side of the park. Everything is covered in snow and ice. '
             'There would normally be flowers, but they are covered by snow. '
             'There is a bench for people to sit on here. Pigeons hop around the ground, looking for scraps.',
    'park5': 'You are at the southeastern side of the park. Everything is covered in snow and ice. '
             'There would normally be flowers, but they are covered by snow. '
             'There is a lamppost here, for illuminating the walkways at night.',
    'park6': 'You are at the southern side of the park. Everything is covered in snow and ice. '
             'There would normally be flowers, but they are covered by snow. '
             'There is a trashcan here.',
    'park7': 'You are at the southwestern side of the park. Everything is covered in snow and ice. '
             'There would normally be flowers, but they are covered by snow. '
             'There is a lamppost here, for illuminating the walkways at night.',
    'park8': 'You are at the western side of the park. Everything is covered in snow and ice. '
             'There would normally be flowers, but they are covered by snow. '
             'There is a bench for people to sit on here.',
    'park9': 'You are at the northwestern side of the park. Everything is covered in snow and ice. '
             'There would normally be flowers, but they are covered by snow. '
             'There is a lamppost here, for illuminating the walkways at night.',
}

#change outdoor object descriptions in winter
room_articles_winter = {
    'yard1': {
        'snow': 'The ground is covered in snow.',
        'fence': 'A standard fence. Its been stained a natural color rather than painted. The tops are covered in '
        'snow.',
        'tree': 'A large cherry tree, typical of this area. It currently has no leaves and is covered in snow.',
        'house': 'Not the largest house on the block, but its a place to live. The roof is covered in snow.',
    },
    'yard2': {
        'snow': 'The ground is covered in snow.',
        'fence': 'A standard fence. Its been stained a natural color rather than painted. The tops are covered in '
        'snow.',
        'mower': 'Its completely rusted out and unusable. You forgot to put it in the shed for the winter again.',
        'push mower': 'Its completely rusted out and unusable. You forgot to put it in the shed for the winter again.',
        'shed': 'A place where you put your tools and spiders set up face traps for you to walk into. It is '
                'locked up for the winter.',
        'gate': 'A simple fence gate leads out. The top is covered in snow.',
    },
    'yard3': {
        'snow': 'The ground is covered in snow.',
        'fence': 'A standard fence. Its been stained a natural color rather than painted. The tops are covered in '
        'snow.',
        'furniture': 'Stackable plastic outdoor furniture. Its covered in a pile of snow.',
    },
    'road1': {
        'snow': 'The ground is covered in snow.',
        'gate': 'A simple fence gate leads out. The top is covered in snow.',
        'fence': 'A standard fence. Its been stained a natural color rather than painted. The tops are covered in '
        'snow.',
        'sidewalk': 'A concrete road bordering a road, designed for pedestrian traffic. Its been freshly shoveled '
                    'off snow, and salted to melt ice away.',
        'road': 'An asphalt road designed for vehicles to drive on. It was recently plowed and covered in sand.',
    },
    'road2': {
        'snow': 'The ground is covered in snow.',
        'fence': 'A standard fence. Its been stained a natural color rather than painted. The tops are covered in '
        'snow.',
        'sidewalk': 'A concrete road bordering a road, designed for pedestrian traffic. Its been freshly shoveled '
                    'off snow, and salted to melt ice away.',
        'road': 'An asphalt road designed for vehicles to drive on. It was recently plowed and covered in sand.',
    },
    'road3': {
        'snow': 'The ground is covered in snow.',
        'fence': 'A standard fence. Its been stained a natural color rather than painted. The tops are covered in '
        'snow.',
        'sidewalk': 'A concrete road bordering a road, designed for pedestrian traffic. Its been freshly shoveled '
                    'off snow, and salted to melt ice away.',
        'road': 'An asphalt road designed for vehicles to drive on. It was recently plowed and covered in sand.',
    },
    'road4': {
        'snow': 'The ground is covered in snow.',
        'fence': 'A standard fence. Its been stained a natural color rather than painted. The tops are covered in '
        'snow.',
        'sidewalk': 'A concrete road bordering a road, designed for pedestrian traffic. Its been freshly shoveled '
                    'off snow, and salted to melt ice away.',
        'road': 'An asphalt road designed for vehicles to drive on. It was recently plowed and covered in sand.',
        'tree': 'A large cherry tree, typical of this area. It currently has no leaves and is covered in snow.',
    },
    'road5': {
        'snow': 'The ground is covered in snow.',
        'fence': 'A standard fence. Its been stained a natural color rather than painted. The tops are covered in '
        'snow.',
        'sidewalk': 'A concrete road bordering a road, designed for pedestrian traffic. Its been freshly shoveled '
                    'off snow, and salted to melt ice away.',
        'road': 'An asphalt road designed for vehicles to drive on. It was recently plowed and covered in sand.',
        'gate': 'A simple fence gate leads out. The top is covered in snow.',
    },
    'road6': {
        'snow': 'The ground is covered in snow.',
        'fence': 'A standard fence. Its been stained a natural color rather than painted. The tops are covered in '
        'snow.',
        'sidewalk': 'A concrete road bordering a road, designed for pedestrian traffic. Its been freshly shoveled '
                    'off snow, and salted to melt ice away.',
        'road': 'An asphalt road designed for vehicles to drive on. It was recently plowed and covered in sand.',
        'park': 'It isn\'t a huge park. Its quiet in the winter here.',
    },
    'road7': {
        'snow': 'The ground is covered in snow.',
        'fence': 'A standard fence. Its been stained a natural color rather than painted. The tops are covered in '
        'snow.',
        'sidewalk': 'A concrete road bordering a road, designed for pedestrian traffic. Its been freshly shoveled '
                    'off snow, and salted to melt ice away.',
        'road': 'An asphalt road designed for vehicles to drive on. It was recently plowed and covered in sand.',
        'park': 'It isn\'t a huge park. Its quiet in the winter here.',
    },
    'park1': {
        'snow': 'The ground is covered in snow.',
        'fountain': 'A large fountain at the center of the park. It is empty of anything but snow and ice for the '
                    'winter right now.',
        'statue': 'A large lion is sitting on a rocky island in the middle of the fountain. It is capped with '
                  'snow and icicles hang underneath it.',
        'lion': 'A large lion is sitting on a rocky island in the middle of the fountain. It is capped with '
                  'snow and icicles hang underneath it.',
        'walkway': 'A paved concrete sidewalk for pedestrians that leads you around the park. Its icy in '
                   'patches where the snow doesn\'t melt.',
    },
    'park2': {
        'snow': 'The ground is covered in snow.',
        'walkway': 'A paved concrete sidewalk for pedestrians that leads you around the park. Its icy in '
                   'patches where the snow doesn\'t melt.',
        'trashcan': 'This particular trashcan is stuffed full beyond capacity. Some of its contents have spilled '
                    'onto the ground.',
        'pigeons': 'These \'flying rats\' are here scavenging food from the overstuffed trashcan.',
    },
    'park3': {
        'snow': 'The ground is covered in snow.',
        'walkway': 'A paved concrete sidewalk for pedestrians that leads you around the park. Its icy in '
                   'patches where the snow doesn\'t melt.',
        'lamppost': 'A tall lamppost with a flower pot hung from a hook on the post. Icicles hang from the lamp and '
                    'the flower pot. Nothing is growing in the pot right now.',
    },
    'park4': {
        'snow': 'The ground is covered in snow.',
        'walkway': 'A paved concrete sidewalk for pedestrians that leads you around the park. Its icy in '
                   'patches where the snow doesn\'t melt.',
        'bench': 'A place to sit. This bench is cold, infested with a flock of Pigeons, and covered in droppings. Not '
                 'the nicest place to sit currently, on second thought.',
        'pigeons': 'These \'flying rats\' are here doing pigeon things and making a mess on the bench.',
    },
    'park5': {
        'snow': 'The ground is covered in snow.',
        'walkway': 'A paved concrete sidewalk for pedestrians that leads you around the park. Its icy in '
                   'patches where the snow doesn\'t melt.',
        'lamppost': 'A tall lamppost with a flower pot hung from a hook on the post. Icicles hang from the lamp and '
                    'the flower pot. Nothing is growing in the pot right now.',
    },
    'park6': {
        'snow': 'The ground is covered in snow.',
        'walkway': 'A paved concrete sidewalk for pedestrians that leads you around the park. Its icy in '
                   'patches where the snow doesn\'t melt.',
        'trashcan': 'This particular trashcan looks like it still has some room left inside.',
    },
    'park7': {
        'snow': 'The ground is covered in snow.',
        'walkway': 'A paved concrete sidewalk for pedestrians that leads you around the park. Its icy in '
                   'patches where the snow doesn\'t melt.',
        'lamppost': 'A tall lamppost with a flower pot hung from a hook on the post. Icicles hang from the lamp and '
                    'the flower pot. Nothing is growing in the pot right now.',
    },
    'park8': {
        'snow': 'The ground is covered in snow.',
        'walkway': 'A paved concrete sidewalk for pedestrians that leads you around the park. Its icy in '
                   'patches where the snow doesn\'t melt.',
        'bench': 'A place to sit. This bench is located in a usually quiet side of the park. Its covered '
                 'in snow right now, and hasn\'t seen any usage in a while from the looks of it.',
    },
    'park9': {
        'snow': 'The ground is covered in snow.',
        'walkway': 'A paved concrete sidewalk for pedestrians that leads you around the park. Its icy in '
                   'patches where the snow doesn\'t melt.',
        'lamppost': 'A tall lamppost with a flower pot hung from a hook on the post. Icicles hang from the lamp and '
                    'the flower pot. Nothing is growing in the pot right now.',
    },
}

#Data on if a room is indoor or outdoor.
room_outside = {
    'bedroom': False,
    'closet': False,
    'hall1': False,
    'hall2': False,
    'hall3': False,
    'bathroom1': False,
    'office': False,
    'entryway': False,
    'bathroom2': False,
    'hall4': False,
    'livingroom': False,
    'diningroom': False,
    'kitchen': False,
    'porch': True,
    'yard1': True,
    'yard2': True,
    'yard3': True,
    'road1': True,
    'road2': True,
    'road3': True,
    'road4': True,
    'road5': True,
    'road6': True,
    'road7': True,
    'park1': True,
    'park2': True,
    'park3': True,
    'park4': True,
    'park5': True,
    'park6': True,
    'park7': True,
    'park8': True,
    'park9': True,
}

#initialize dictionary to handle encounters outside
encounter_table = {
    'porch': 'nothing',
    'yard1': 'nothing',
    'yard2': 'nothing',
    'yard3': 'nothing',
    'road1': 'nothing',
    'road2': 'nothing',
    'road3': 'nothing',
    'road4': 'nothing',
    'road5': 'nothing',
    'road6': 'nothing',
    'road7': 'nothing',
    'park1': 'nothing',
    'park2': 'nothing',
    'park3': 'nothing',
    'park4': 'nothing',
    'park5': 'nothing',
    'park6': 'nothing',
    'park7': 'nothing',
    'park8': 'nothing',
    'park9': 'nothing',
}