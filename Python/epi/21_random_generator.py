import random

def random_iterator(limit):
    offset = 0 
    while True:
        offset += random.random()
        if offset > limit:
            raise StopIteration()
        yield offset

if __name__ == '__main__':
    result = random_iterator(5)
    print result
