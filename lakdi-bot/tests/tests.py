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

    cards = generate_cards()
    print cards
    for card in CARDS.TYPE:
        print card, ">>>>>>"
        predicted_hands = bot.predict_hands(cards, card)
        print predicted_hands
test_predict_hands()
