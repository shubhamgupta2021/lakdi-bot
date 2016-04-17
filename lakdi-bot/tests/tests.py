from ..src.bot import Bot
from ..src.constants import CARDS


def test_predict_hands():
    bot = Bot()
    cards = ["s_2", "s_3", "s_A", "d_A", "d_K", "d_Q", "d_10", "h_9", "h_10",
             "h_K", "h_J", "h_Q", "c_K"]
    for card in CARDS.TYPE:
        print card, ">>>>>>"
        test_predict_hands = bot.predict_hands(cards, card)

test_predict_hands()
