import logging
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton)
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import random
import os
import time 

IMAGES = ['''

    +---+
    |
    
    
    
    
    
        ''', '''

    +---+
    |
    😕
    
    
    
            
        ''', '''

    +---+
    |
    🙁
    |
    
    
            
        ''', '''

    +---+
    |
    ☹️
   /|
    
    
        
        ''', '''

    +---+
    |
    😧
   /|\ 
    
    
               
        ''', '''

    +---+
    |
    😩
   /|\ 
    |
    
           
        ''', '''

    +---+
    |
    😨 
   /|\  
    |   
   /  
                
        ''', '''

    +---+
    |
    💀
   /|\ 
    |
   / \ 
            
        ''', '''

''']

WORDS = [
    'cuadriplejia', 
    'higiene',
    'procedimiento',
    'descomponer',
    'algoritmo',
    'ligamento',
    'plaguicida',
    'creatividad',
    'rodilla',
    'paralelepipedo',
    'informatica',
    'belgica'
]