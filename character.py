# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

class Character():

    
    
    # Create a character
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None
        #self.presence_rooms = {} # tranferred to Room classe
        #self.figth_ready="no"  #overrided by Enemy subclass creation

    #def get_name(self):
    #    return self.name
    
    #def name(self):
    #    print( self.name)
  
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    
    def get_description(self):
        return self.description
       
    def set_description(self, item_description):
        self.description = item_description

    # Describe this character
    def describe(self):
        print( self.name + " is here!" )
        print( self.description )
        
    def get_details(self):
        #obolte as gettet and setter methods were drop
        #print(self.get_name())
        print(self.name)
        print(self.get_description())
    
    
    #def presence_show(self):
        
    #    print(self.presence_rooms())  
        
        
    #def set_presence(self,room_name):
       
    #    if room_name not in self.presence_rooms:
    #        self.presence_rooms[room_name]="yes"
    #    else:
    #        print(self.get_name(), "already in ", room_name)

    #def drop_presence(self,room_name):
       
    #    if room_name in self.presence_rooms:
    #        self.presence_rooms.pop(room_name)
    #    else:
    #        print(self.get_name(), "not in ", room_name)
            
        
        #itera el diccionario (keys)
    #    for presence in self.presence_rooms:
    #        #recupero la referencia deroom segun las direcciones (keys) del diccionario linked_rooms
    #       room = self.presence_rooms[presence]
    #        print( "The " + self.get_name() + " is in  " + presence)    
        
    # Set what this character will say when talked to
    def set_conversation(self, conversation):
        self.conversation = conversation

            
    # Talk to this character
    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

    # Fight with this character
    def fight(self, combat_item):
        
        print(self.name + " doesn't want to fight with you")
        return True
                
    
class Enemy(Character):
    
    
    number_of_enemies = 0
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None
        self.figth_ready="yes"
        self.gun = None
        Enemy.number_of_enemies = Enemy.number_of_enemies + 1
        
    def set_weakness(self, enemy_weakness):
        self.weakness = enemy_weakness

    def get_weakness(self):
        return self.weakness

    def fight(self, combat_item):
        if combat_item == self.weakness:
            print("You fend " + self.name + " off with the " + combat_item )
            return True
        else:
            print(self.name + " crushes you, puny adventurer")
            return False

class Friend(Character):

    def __init__(self, char_name, char_description):

        super().__init__(char_name, char_description)
        self.feeling = None
        

    def hug(self):
        print(self.name + " hugs you back!")

    # What other methods could your Friend class have?


        