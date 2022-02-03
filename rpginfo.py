#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 17:04:13 2022

@author: josep
"""

class RPGInfo():
        
    author = "Anonymous"
    
    def __init__(self, game_title):
        self.title = game_title
   
    def welcome(self):
        print("Welcome to " + self.title)

    @staticmethod
    def info():
        print("Made using the OOP RPG game creator (c) me")        
        
    @classmethod
    def credits(cls):
        print("Thank you for playing")
        print("Created by " + cls.author)        