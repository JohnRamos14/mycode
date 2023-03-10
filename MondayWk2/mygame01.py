#!/usr/bin/python3
"""Driving a simple game framework with
   a dictionary object | Alta3 Research"""

def showInstructions():
    """Show the game instructions when called"""
    #print a main menu and the commands
    print('''
    RPG Game
    ========
    Commands:
      go [direction]
      get [item]
    ''')

def showStatus():
    """determine the current status of the player"""
    # print the player's current location
    print('---------------------------')
    print('You are in the ' + currentRoom)
    # print what the player is carrying
    print('Inventory:', inventory)
    # check if there's an item in the room, if so print it
    if "item" in rooms[currentRoom]:
      print('You see a ' + rooms[currentRoom]['item'])
    print("---------------------------")


# an inventory, which is initially empty
inventory = []

# a dictionary linking a room to other rooms
rooms = {

            'Hall' : {
                  'south' : 'Kitchen',
                  'east' : 'Dinning Room',
                  'item' : 'key'
                },

            'Kitchen' : {
                  'north' : 'Hall',
                  'item' : 'monster',
                },
            
            'Dinning Room': {
                'west': 'Hall',
                'south' : 'Garden',
                'item' : 'potion'
                },

            'Garden' : {
                'north' : 'Dinning Room'
         }
    }

# start the player in the Hall
currentRoom = 'Hall'

showInstructions()

# breaking this while loop means the game is over
while True:
    showStatus()

    # the player MUST type something in
    # otherwise input will keep asking
    move = ''
    while move == '':  
        move = input('>')

    # normalizing input:
    # .lower() makes it lower case, .split() turns it to a list
    # therefore, "get golden key" becomes ["get", "golden key"]          
    move = move.lower().split(" ", 1)

    #if they type 'go' first
    if move[0] == 'go':
        #check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            #set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        # if they aren't allowed to go that way:
        else:
            print('You can\'t go that way!')

    #if they type 'get' first
    if move[0] == 'get' :
        # make two checks:
        # 1. if the current room contains an item
        # 2. if the item in the room matches the item the player wishes to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            #add the item to their inventory
            inventory.append(move[1])
            #display a helpful message
            print(move[1] + ' got!')
            #delete the item key:value pair from the room's dictionary
            del rooms[currentRoom]['item']
        # if there's no item in the room or the item doesn't match
        else:
            #tell them they can't get it
            print('Can\'t get ' + move[1] + '!')


    ## If a player enters a room with a monster
    if rooms.get(currentRoom).get('item') == 'monster':
        print('A monster has got you... GAME OVER!')
        break

    ## Defube giw a player can win
    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('You escaped the house with the ultra rare key and magic potion... YOU WON!')

    # Define player's health
    player_health = 100

    # Define the monster's health
    monster_health = 50

    #Check if there's a monster in the room
    if rooms.get(currentRoom).get('item') == 'monster':
        print('A monster has appeared!')
        print(f'Player Health: {player_health}')
        print(f'Monster Health: {monster_health}')
        while player_health > 0 and monster_health > 0:
            print('What do you want to do? [fight/run]')
            action = input()
            if action == 'fight':
                print('You attack the monster!')
                monster_health -= 10
                if monster_health <= 0:
                    print('You killed the monster!')
                    del rooms[currentRoom]['item']
                    break
                else:
                    print(f'Monster Health: {monster_health}')
                    print('The monster counterattacks!')
                    player_health -= 5
                    print(f'Player Health: {player_health}')
            elif action == 'run':
                print('You run away from the monster')
                break
        if player_health <= 0:
            print('A monster has got you... GAME OVER!')
            break


