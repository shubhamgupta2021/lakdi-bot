from .classes import IteratableConstants

class CARDS(object):

    CAN_WIN = ["K", "Q"]

    CONFIRM_WIN = ["A"]

    class TYPE(IteratableConstants):
        SPADE = "s"
        CLUB = "c"
        DIAMOND = "d"
        HEART = "h"

    VALUE = { "2": 1,
             "3": 2,
             "4": 3,
             "5": 4,
             "6": 5,
             "7": 6,
             "8": 7,
             "9": 8,
             "10": 9,
             "J": 10,
             "Q": 11,
             "K": 12,
             "A": 13}

