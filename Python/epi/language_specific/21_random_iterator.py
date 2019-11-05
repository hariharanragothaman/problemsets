import random

class RandomIncrement():
    def __init__(self, limit):
        self._offset = 0.0
        self._limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        self._offset = random.random()
        if self._offset > self._limit:
            raise StopIteration
        return self._offset

    def increment_limit(self, increment_amount):
        self._limit += increment_amount

if __name__ == '__main__':
    r1 = RandomIncrement(5)
    result = r1.__next__()
    print result
