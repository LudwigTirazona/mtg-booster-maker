#!/usr/bin/python3

import random

cards = {
    'green': 0,
    'white': 0,
    'blue': 0,
    'red': 0,
    'gold': 0,
    'colorless': 0
}

cards['green'] = int(input('\n# of Green cards: '))
cards['white'] = int(input('# of White cards: '))
cards['blue'] = int(input('# of Blue cards: '))
cards['black'] = int(input('# of Black cards: '))
cards['red'] = int(input('# of Red cards: '))
cards['gold']= int(input('# of Gold/Hybrid cards: '))
cards['colorless'] = int(input('# of colorless cards: '))

boost_size = int(input('# of cards per booster pack: '))

booster_index = 0
booster_counter = 0
boost_again = True
boost_success = True

while boost_again:
    booster_counter += 1
    print ("\nGenerating booster pack #" + str(booster_counter) + "\n")
    boost_query = ' '
    for booster_index in range(0, boost_size):
        if sum(cards.values()) == 0 :
            boost_success = False
            print("Insufficient cards to complete booster pack.\n")
            break

        card_selected = random.choice([color for color in cards if cards[color] > 0])
        cards[card_selected] -= 1

        print( str(booster_index + 1) + ". ) " + card_selected.capitalize())

    if boost_success :
        print("\nBooster pack complete.\n")

    while (boost_query.lower() != 'y' and boost_query.lower() != 'n'):

        boost_query = input('Create a new booster pack? (y/n)')

        if (boost_query == 'N' or boost_query == 'n'):
            boost_again = False
