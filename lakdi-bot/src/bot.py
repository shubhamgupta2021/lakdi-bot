from .constants import CARDS


class Bot(object):

    def predict_hands(self, my_cards, trump):
        can_win_cards = dict()
        no_trump_win_cards = 0
        no_cards = dict()
        no_winning_cards = dict()
        for type_ in CARDS.TYPE:
            no_cards[type_] = 0
            no_winning_cards[type_] = 0
            can_win_cards[type_] = []

        for card in my_cards:
            type_, value = card.split("_")
            no_cards[type_] += 1
            if value in (CARDS.CAN_WIN + CARDS.CONFIRM_WIN):
                no_winning_cards[type_] += 1
                can_win_cards[type_] += value

        total_hands = 0

        for type_ in CARDS.TYPE:
            if type_ != trump:
                if no_cards[type_] == 1 and can_win_cards[type_] != CARDS.CONFIRM_WIN:
                    no_winning_cards[type_] = 0
                if no_cards[type_] >=5 and no_winning_cards[type_]>=2:
                    no_winning_cards[type_] = 1
                elif no_cards[type_] >3 and no_winning_cards[type_]>=3:
                    no_winning_cards[type_] = 2
            else:
                if no_cards[type_] == 1 and can_win_cards[type_] != CARDS.CONFIRM_WIN:
                    no_winning_cards[type_] = 0
                if no_cards[type_]-no_winning_cards[type_] > 1:
                    no_winning_cards[type_] += int((no_cards[type_] -
                                                no_winning_cards[type_])/1.5)
            total_hands += no_winning_cards[type_]
        print no_winning_cards
        return total_hands
