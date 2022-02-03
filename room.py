#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 15:29:19 2022

@author: josep
"""

class Room():
    
    
    #variable de clase se crea fura del constructor
    number_of_rooms = 0
    
    def __init__(self,room_name):  #constructor method
   
        self.name = room_name #anyado atributos 
        self.description = None #anyado atributos
        self.linked_rooms = {} #creq undiccionario vacio
        self.character = None
        self.item = None
        #self.presence_item = {} #obsolete transfered to Room class
        Room.number_of_rooms = Room.number_of_rooms + 1
        
    #definicion de metodos       
    def set_description(self, room_description):
        self.description = room_description
    
    def get_description(self):
        return self.description
    
    def describe(self):
        print( self.description )
        
        
    def set_name(self, room_name):
        self.name = room_name
    
    def get_name(self):
        return self.name
    
    def set_character(self, new_character):
        self.character = new_character
    
    def get_character(self):
        return self.character
    
    def set_item(self, new_item):
        self.item = new_item
    
    def get_item(self):
        return self.item
    
    def drop_item(self):
        self.item = None
        
    
    
    
    
    def name(self):
        print( self.name)
        
    def link_room(self, room_to_link, direction):
        
        self.linked_rooms[direction] = room_to_link #asi me aparece la referenmci
        #self.linked_rooms[direction] = room_to_link.get_name() # así el nombre pero falla en get_details`
        #para mostrar como prueba
        #print( self.name + " linked rooms :" + repr(self.linked_rooms) )
    
    def get_details(self):
        print(self.get_name())
        print(self.get_description())
        
        #itera el diccionario (keys)
        for direction in self.linked_rooms:
            #recupero la referencia deroom segun las direcciones (keys) del diccionario linked_rooms
            room = self.linked_rooms[direction]
            print( "The " + room.get_name() + " is " + direction)   
        if self.item is not None:
            print(self.item.get_details())
            
            
    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way")
            return self            