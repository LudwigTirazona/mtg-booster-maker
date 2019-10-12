#!/usr/bin/python3

import random
from itertools import chain, repeat

cards = {
    'green': 0,
    'white': 0,
    'blue': 0,
    'red': 0,
    'gold': 0,
    'colorless': 0
}

def set_cards():
    for color in cards:
        prompt_string = '# of {} cards: '.format(color.capitalize())

        prompts = chain([prompt_string], repeat("Not a valid number. Try again: "))
        replies = map(input, prompts)
        valid_response = next(filter(str.isdigit, replies))

        cards[color] = int(valid_response)

    return cards


set_cards()
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
        card_total = sum(cards.values())
        if card_total == 0 :
            boost_success = False
            print("Insufficient cards to complete booster pack.\n")
            break

        card_selected = random.choice([color for color in cards if cards[color] > 0])
        cards[card_selected] -= 1

        print( str(booster_index + 1) + ". ) " + card_selected.capitalize())

    if boost_success :
        print("\nBooster pack complete.\n")

    while (boost_query.lower() != 'y' and boost_query.lower() != 'n'):

        if card_total == 0:
            print('Not enough remaining cards to complete a booster pack')
            print('\nExiting program.')
            boost_query = 'n'
        else:
            boost_query = input('Create a new booster pack? (y/n)')

        if boost_query.lower() == 'n':
            boost_again = False
