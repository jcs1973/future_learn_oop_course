#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 15:37:44 2022

@author: josep
"""

#No medeja importarlo desde roomJCoca.py ¿?
from room import Room
from item import Item
from character import Character
from character import Enemy
from character import Friend
from rpginfo import RPGInfo



spooky_castle = RPGInfo("The Spooky Castle")
spooky_castle.welcome()
RPGInfo.info()

RPGInfo.author = "Raspberry Pi Foundation"
RPGInfo.credits()





sword=Item("Sword")
#sword.name

#Obsolete Item presence tranfered to Room
#sword.set_presence(kitchen.name)
#sword.set_presence(dining_hall.name)
#sword.set_presence(ballroom.name)
#sword.drop_presence(ballroom.name)
sword.set_description("Sharp sword")
#sword.describe()
#sword.get_details()


hammer=Item("Hammer")
#Obsolete Item presence tranfered to Room
#hammer.set_presence(kitchen.name)
#hammer.set_presence(ballroom.name)
hammer.set_description("Big hammer to hit")
#hammer.describe()
#hammer.get_details()

corkscrew=Item("Corkscrew")
corkscrew.set_description("Unuseful item")



kitchen = Room("kitchen")
ballroom = Room("ballroom")
dining_hall = Room("dining_hall")


#print(kitchen)
#kitchen.get_description()


#kitchen.set_name('kitchen')
kitchen.set_description('Dirty room')
ballroom.set_description('Unpleasant place to dance')

dining_hall.set_description('Scary dinning hall')
#dining_hall.set_name('dinning hall')

#kitchen.name
#kitchen.describe()

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")


#current_room = kitchen          

#while True:		
    #print("\n")         
    #current_room.get_details()         
    #command = input("> ")    
    #current_room = current_room.move(command)  



dave =Enemy("Dave", "A smelly zombie")

dave.set_conversation("What do you want?")
#dave.set_presence(kitchen.name)
dave.set_weakness(hammer.name)
#dave.describe()
#dave.get_details()

#dave.talk()
#dave.fight(sword.name)

john=Enemy("John","A agressive zomby")

#john.describe()
#john.talk()
#john.get_details()
john.set_conversation("I am John")
#john.set_presence(ballroom.name)
#john.figth_ready overrided
#john.weakness
john.set_weakness(sword.name)
#john.fight("")
#john.fight(sword.name)

mark=Friend("Mark","A friendly nome")

#mark.describe()
#mark.talk()
#mark.get_details()
mark.set_conversation("I am Mark, good to see you!!!")
#john.set_presence(ballroom.name)



#print("What will you fight with?")
#fight_with = input()
#john.fight(fight_with)

dining_hall.set_character(john)
kitchen.set_character(dave)
ballroom.set_character(mark)


dining_hall.set_item(hammer)
kitchen.set_item(corkscrew)
ballroom.set_item(sword)


#as a list or a dictionary keys time name:item object?
backpack = []

current_room=ballroom
dead=False
defeated=0
while dead ==False:
    
    test_weapon=False
    print("\n")         
    current_room.get_details()
    inhabitant = current_room.get_character()
    item = current_room.get_item()
    
    # Add your code here

    if inhabitant is not None:
        inhabitant.describe()
    if item is not None:
        item.get_details()
        
    command = input("> ")    
    
   # Check whether a direction was typed
    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)
   
    elif command == "talk":
        # Add code here
        
        if inhabitant is not None:
            #inhabitant.get_details()
            inhabitant.talk()
        else:
            print("No one is in the room")
        
    elif command == "fight": 
        
        
        if inhabitant is not None:
            
            if isinstance(inhabitant, Enemy):
                inhabitant.get_details()
                print("choose weapon")
                weapon = input("> ")
                
                test_weapon=weapon in backpack
                
                #if weapon in backpack:
                if test_weapon:
                    
                    if inhabitant.fight(weapon) == True:
                        current_room.set_character(None)
                        defeated=defeated+1
                        dead=False
                        if Enemy.number_of_enemies == defeated:
                            print("You win the game, all the enemies have defeated")
                            dead=True
                    else:
                        print("Oh dear, you lost the fight.")
                        dead=True
                else:
                    print("Yo don't have "+weapon+" to fight")
                    print("choose weapon")
                    weapon = input("> ")         
                    
            else:
                print("choose weapon")
                weapon = input("> ")
                inhabitant.fight(weapon)
                
                
        else:
            print("No one is in the room")
                
 
        
    elif command == "hug": 
        
        
        if inhabitant is not None and isinstance(inhabitant, Friend):
           
           inhabitant.hug()
            
        else:
            print("I don't like you")
                
    elif command == "take": 
        
        
        if item is not None:

           print("You got  the "+ item.get_name()) 
           backpack.append(item.get_name())
           current_room.drop_item()
            
        else:
            print("There is no object in this room")
                
        
RPGInfo.credits()
        
        