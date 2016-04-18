import random

from ..src.bot import Bot
from ..src.constants import CARDS
values  = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
suites = ["s", "h", "d", "c"]

def test_predict_hands():
    bot = Bot()
    def generate_cards():
        cards = set()
        while len(cards) !=13:
            value = random.choice(values)
            suite = random.choice(suites)
            card = "{}_{}".format(suite, value)
            cards.add(card)
        return cards

    #cards = generate_cards()
    cards = ["s_2", "s_3", "s_A", "d_A", "d_K", "d_Q", "d_10", "h_9", "h_10",
             "h_K", "h_J", "h_Q", "c_A"]
    print cards
#    for card in CARDS.TYPE:
#       print card, ">>>>>>"
    predicted_hands = bot.predict_hands(cards, "h")
test_predict_hands()
