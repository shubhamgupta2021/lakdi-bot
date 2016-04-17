class __IteratableConstanstsMeta__(type):
    def __iter__(self):
        for attr in dir(self):
            if not attr.startswith("__"):
                yield getattr(self, attr)

class IteratableConstants(object):
    __metaclass__ = __IteratableConstanstsMeta__
