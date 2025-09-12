"""
Learning notes and daily Python practice.
This file documents my progress and code written on September 10, 2025.
"""

import random

# create a variable to represent my name
my_first_name = str('Christian Ventura')

# create a variable to represent my favorite MTG set
favorite_MTG_set = str('Khans of Tarkir')

# create a variable to represent the number of decks I own
num_of_decks_i_own = int(6)

# print(f'My name is {my_first_name}.\nMy favorite Magic: the Gathering set is {favorite_MTG_set}.\nI currently own {num_of_decks_i_own} decks.')

# create a list of card names. If the card entered is in list, stop printing the list. 
# favorite_card_names = ['Dark Ritual', 'Thoughtseize', 'Chulane, Teller of Tales', 'Ugin, the Spirit Dragon', 'Damnation', 'Timetwister' ,'Mana Crypt', 'Stormbreath Dragon']

# for card in favorite_card_names:
#     if card == 'Timetwister':
#         break
#     else:
#         print(card)

# this script asks for an input as a color of mana and returns the value stored in each variable based on the color inputted. 
blue_card ='Ancestral Recall'
black_card = 'Dark Ritual'
red_card = 'Lightning Strike'
green_card = 'Green Dragon'
white_card = 'Swords to Plowshares'

result = input('Please enter a color of mana or exit: ')
if result == 'blue':
    print(blue_card)
elif result =='black':
        print(black_card)
elif result == 'white':
        print(white_card)
elif result == 'red':
    print(red_card)
elif result == 'green':
    print(green_card)
else:
    print("Thanks for using the program.")

