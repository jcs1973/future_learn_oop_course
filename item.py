#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 10:12:21 2022

@author: josep
"""

class Item():
    def __init__(self,item_name):  #constructor method
   
        self.name = item_name #anyado atributos 
        self.description = None #anyado atributos
        #self.presence_rooms = {} #obsolete transfered to Room class

  #definicion de metodos       
    def set_description(self, item_description):
        self.description = item_description
    
    def get_description(self):
        return self.description
    
    def describe(self):
        print( self.description )
        
        
    def set_name(self, item_name):
        self.name = item_name
    
    def get_name(self):
        return self.name
    
    def name(self):
        print( self.name)
  
       
    def presence_show(self):
        
        print(self.presence_rooms())  
        
        
    def get_details(self):
        print(self.get_name())
        print(self.get_description())
        
        #Obsolete Item presence tranfered to Room
        #for presence in self.presence_rooms:
            #recupero la referencia deroom segun las direcciones (keys) del diccionario linked_rooms
        #    room = self.presence_rooms[presence]
        #    print( "The " + self.get_name() + " is in  " + presence)            
    
    #obsolete transfered to Room class
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
    
    
    
    
    
    
    
    