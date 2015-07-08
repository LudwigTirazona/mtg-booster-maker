#!/usr/bin/python
#################################################################################
# Copyright (C) 2015  Ludwig Tirazona
# 
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
##################################################################################

####################################################################
# Author: Ludwig Tirazona <ljtirazona at gmail dot com>
# Latest update: 26 Jun 2015
# Description: Input the amount of each type of card that you have, 
#              and the number of cards per booster pack you wish to 
#              generate. Booster Maker will do the rest.
####################################################################

import random
## Init section
#TODO Allow to initialize using command-line args
#print ( sys.argv )
#TODO Allow to initialize using text files
# If no command-line arguments.
#TODO Calculate number of rares and uncommons per booster.
#rares = int( raw_input('# of Rare cards: ') )
#uncommons = int( raw_input('# of Uncommon cards: ') )
green_index = int( raw_input('\n# of Green cards: ') )
white_index  = int( raw_input('# of White cards: ') ) + green_index
blue_index  = int( raw_input('# of Blue cards: ') ) + white_index
black_index  = int( raw_input('# of Black cards: ') ) + blue_index
red_index  = int( raw_input('# of Red cards: ') ) + black_index
gold_index  = int( raw_input('# of Gold/Hybrid cards: ') ) + red_index
colorless_index  = int( raw_input('# of colorless cards: ') ) + gold_index
boost_size = int( raw_input('# of cards per booster pack: ') )

#DEBUG print ("Red index: " + str(red_index) + "\n")
## Init section END
booster_index = 0
booster_counter = 0
boost_again = True
boost_success = True
while boost_again:
	booster_counter += 1
	print ("\nGenerating booster pack #" + str(booster_counter) + "\n")
	boost_query = ' '
	for booster_index in range(0, boost_size):
		if colorless_index == 0 :
			boost_success = False
			print("Insufficient cards to complete booster pack.\n")
			break
		card_selected = random.randint(1,colorless_index)
		#DEBUG print ('Number generated: ' + str(card_selected) )
		if card_selected <= green_index:
			print( str(booster_index + 1 ) + ".) Green" )
			green_index -= 1
			white_index -= 1
			blue_index -= 1
			black_index -= 1
			red_index -= 1
			gold_index -= 1
			colorless_index -= 1
		else:
			if (card_selected > green_index and card_selected <= white_index):
				print( str(booster_index + 1 ) + ".) White")
				white_index -= 1
				blue_index -= 1
				black_index -= 1
				red_index -= 1
				gold_index -= 1
				colorless_index -= 1
			else:
				if (card_selected > white_index and card_selected <= blue_index):
					print( str(booster_index + 1 ) + ".) Blue")
					blue_index -= 1
					black_index -= 1
					red_index -= 1
					gold_index -= 1
					colorless_index -= 1
				else:
					if (card_selected > blue_index and card_selected <= black_index):
						print( str(booster_index + 1 ) + ".) Black")
						black_index -= 1
						red_index -= 1
						gold_index -= 1
						colorless_index -= 1
					else:
						if (card_selected > black_index and card_selected <= red_index):
							print( str(booster_index + 1 ) + ".) Red")
							red_index -= 1
							gold_index -= 1
							colorless_index -= 1
						else:
							if (card_selected > red_index and card_selected <= gold_index):
								print( str(booster_index + 1 ) + ".) Gold")
								gold_index -= 1
								colorless_index -= 1
							else:
								if (card_selected > gold_index and card_selected <= colorless_index):
									print( str(booster_index + 1 ) + ".) Colorless")
									colorless_index -= 1
	if boost_success :
		print("\nBooster pack complete.\n")
	while (boost_query != 'Y' and boost_query != 'y' and boost_query != 'N' and boost_query != 'n'): 
		boost_query = raw_input('Create a new booster pack? (y/n)')									
	#TODO Pick-up from here
        if (boost_query == 'N' or boost_query == 'n'):
		boost_again = False
		
