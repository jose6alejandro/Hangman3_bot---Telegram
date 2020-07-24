import logging
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton)
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import random
import os
import time 
from images import *

def start_command(update, context):
    game_data['state_game'] = True
    game_data['word'] = random_word()
    game_data['spaces'] = ['_'] * len(game_data['word'])
    game_data['life'] = 0
    game_data['letter_aux'] = []
    #print(game_data['word']) 
    game(update, context)


def help_command(update, context):
    update.message.reply_text(
    ''' Este es un mini-Bot para jugar el famoso juego de adivinanzas el ahorcado.

    Comandos:

    /start - comienza el juego. Se genera una palabra la cual debe adivinar ingresando \
    letra por letra hasta completarla.

    /stop - termina el juego. Si desea jugar nuevamente, debe ingresar el comando anterior.

    by. @jose6alejandro

    ''')

def stop_command(update, context):
    game_data['state_game'] = False
    update.message.reply_text('Se ha detenido el bot. Use /start para iniciar otra partida')

def random_word():
 	return words[random.randint(0, len(words) - 1)][:-1]

def display_board(update, context, game_data):
    
    keyboard = [['A', 'B', 'C', 'D', 'E', 'F', 'G'], 
                ['H', 'I', 'J', 'K', 'L', 'M', 'N'], 
                ['O', 'P', 'Q', 'R', 'S', 'T', 'U'], 
                ['V', 'W', 'X', 'Y', 'Z']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=False, resize_keyboard=True)
    update.message.reply_text(IMAGES[game_data['life']] + " ".join(game_data['spaces']) + '\n\n' + 'Presione una tecla''', reply_markup=reply_markup)


def game(update, context, **kwargs):

    if game_data['state_game']:

        current_letter = update.message.text.lower()
        if (len(current_letter) > 1):
            display_board(update, context, game_data)
        else:

            letter_index = [i for i in range(len(game_data['word'])) if game_data['word'][i] == current_letter]

            if len(letter_index) <= 0:    
                game_data['life']+= 1

                for i in range(len(game_data['letter_aux'])):
                    if game_data['letter_aux'][i] == current_letter:
                        update.message.reply_text('La letra {} ya la usaste'.format(current_letter.upper()))
                        game_data['life']-= 1
                        break
            
                game_data['letter_aux'].append(current_letter)

            else:
                for i in letter_index:
                    game_data['spaces'][i] = current_letter
                
                letter_index = []  

            display_board(update, context, game_data)
            
            if game_data['life'] == 7:
                update.message.reply_text('🤦 Perdiste, la palabra correcta es {}'.format(game_data['word'].upper()))
                game_data['state_game'] = False

            try:
                game_data['spaces'].index('_')

            except ValueError:
                update.message.reply_text('💪 Felicitaciones ganaste! la palabra es {}'.format(game_data['word'].upper()))
                game_data['state_game'] = False
    else:
        update.message.reply_text('Use /start para iniciar el juego')


game_data = {'state_game': False}

with open('words.csv', 'r') as file:
    words = file.readlines()

