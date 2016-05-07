import random
from .constants import CARDS


class Bot(object):
    '''Automatic  stateless player for Lakdi App. It can predit hands based 
    upon cards, also it will play the round.
    '''

    def predict_hands(self, my_cards, trump):
        winning_cards = list()
        no_hands = 0
        no_cards = dict()
        suite_factor = dict()
        for type_ in CARDS.TYPE:
            no_cards[type_] = 0

        for card in my_cards:
            type_, value = card.split("_")
            no_cards[type_] += 1
        print no_cards
        for type_ in CARDS.TYPE:
            if type_ != trump:
                if no_cards[type_] < 5: 
                    suite_factor[type_] = .903 - abs(no_cards[type_] -3)/13.0
                else:
                    suite_factor[type_] = 0.75
            else:
                if no_cards[type_] <= 8: 
                    suite_factor[type_] = (9+no_cards[type_])/13.0
                else:
                    suite_factor[type_] = 1.5

# This is the second method
#            if no_cards[type_] == 1:
#                suite_factor[type_] = 0.75
#            elif no_cards[type_] == 2: 
#                suite_factor[type_] = 0.85
#            elif no_cards[type_] == 3:
#                suite_factor[type_] = 0.9
#            elif no_cards[type_] == 4:
#                if type_ != trump:
#                    suite_factor[type_] = 0.85
#                else:
#                    suite_factor[type_] = 1.1
#            else: 
#                if type_ != trump:
#                    suite_factor[type_] = 3.0/(no_cards[type_]+3)
#                else:
#                    suite_factor[type_] = no_cards[type_]/3.0
# continues till end of this method

        print suite_factor
        for card in my_cards:
            type_, value = card.split("_")
            card_probability = CARDS.VALUE[value]/13.0
            print card
            print "before",
            print card_probability
            card_probability *= suite_factor[type_]
            print "after",
            card_probability = float("{0:.2f}".format(card_probability))
            print card_probability
            if card_probability >= 0.75:
                no_hands += 1
                winning_cards.append(card)
        print winning_cards
        print no_hands

#    def predict_hands(self, my_cards, trump):
#        ''' Predict the hands that it will make in a turn based upon the cards
#        and the trump for that game'''
#
#        can_win_cards = dict()
#        no_trump_win_cards = 0
#        no_cards = dict()
#        no_winning_cards = dict()
#        for type_ in CARDS.TYPE:
#            no_cards[type_] = 0
#            no_winning_cards[type_] = 0
#            can_win_cards[type_] = []
#
#        for card in my_cards:
#            type_, value = card.split("_")
#            no_cards[type_] += 1
#            if value in (CARDS.CAN_WIN + CARDS.CONFIRM_WIN):
#                no_winning_cards[type_] += 1
#                can_win_cards[type_] += value
#
#        total_hands = 0
#
#        for type_ in CARDS.TYPE:
#            if type_ != trump:
#                if no_cards[type_] == 1 and can_win_cards[type_] != CARDS.CONFIRM_WIN:
#                    no_winning_cards[type_] = 0
#                if no_cards[type_] >=5 and no_winning_cards[type_]>=2:
#                    no_winning_cards[type_] = 1
#                elif no_cards[type_] >3 and no_winning_cards[type_]>=3:
#                    no_winning_cards[type_] = 2
#            else:
#                if no_cards[type_] == 1 and can_win_cards[type_] != CARDS.CONFIRM_WIN:
#                    no_winning_cards[type_] = 0
#                if no_cards[type_]-no_winning_cards[type_] > 1:
#                    no_winning_cards[type_] += int((no_cards[type_] -
#                                                no_winning_cards[type_])/1.5)
#            total_hands += no_winning_cards[type_]
#        print no_winning_cards
#        return total_hands

    def play_chance(self, trump, my_cards, cards_played):
        
        def isolate_cards(all_cards):
            cards = dict()
            for type_ in CARDS.TYPE:
                cards[type_] = list()

            for card in all_cards:
                card_type, card_value = card.split("_")
                cards[card_type].append(card)
            return cards


        def find_smallest_card(cards, generic=False):
            if not cards:
                raise ValueError("Card list cannot be empty")
            cards_to_search = cards
            if generic:
                type_cards = isolate_cards(cards)
                least_length = 14
                for type_ in type_cards:
                    if len(type_cards[type_]) and len(type_cards[type_]) < least_length:
                        least_length = len(type_cards[type_])
                        cards_to_search = type_cards[type_]
                    elif len(type_cards[type_]) and len(type_cards[type_]) == least_length:
                        possible_card_1 = find_smallest_card(cards_to_search)
                        possible_card_2 = find_smallest_card(type_cards[type_]) 
                        possible_card_1_type, possible_card_1_value = possible_card_1.split("_")
                        possible_card_2_type, possible_card_2_value = possible_card_2.split("_")
                        if int(possible_card_1_value) > int(possible_card_2_value):
                            cards_to_search = type_cards[type_]
                        elif int(possible_card_1_value) == int(possible_card_2_value):
                            if random.choice((True, False)):
                                cards_to_search = type_cards[type_]
 
            smallest_card_value = 13
            search_card_type, value = cards_to_search[0].split("_")
            for card in cards_to_search:
                card_type, card_value = card.split("_")
                card_value = int(card_value)
                if card_type != search_card_type:
                    raise ValueError("Cards does not contain similar suites"
                                     "card")
                if card_value < smallest_card_value:
                    smallest_card_type = card_type
                    smallest_card_value = card_value
                    smallest_card = card
                elif card_value == smallest_card_value:
                    raise TypeError("Two similar cards")
            
            return smallest_card


        chance = len(cards_played)+1
        cards = isolate_cards(my_cards)
        if chance != 1:
            chance_card_type, value = cards_played[0].split("_")
            if cards[chance_card_type]:
                for card in cards[chance_card_type]:
                    win_probability()
            elif cards[trump]:
                for card in cards[trump]:
                    win_probability(trump=True)
            else:
                other_cards = []
                for key, value in cards.iteritems():
                    if key not in (chance_card_type, trump):
                        other_cards += value
                return find_smallest_card(other_cards, generic=True)

