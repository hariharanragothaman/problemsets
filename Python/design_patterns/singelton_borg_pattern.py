"""
Borg Pattern: Monostate pattern

Implement singelton behavior --- instead of one instance, have mulitple instance that share the same state
Focus is on sharing state, instead of sharing instance identity.
"""

class Borg:
    __shared_state = {}

    def __init__(self):
        self.__dict__ = self.__shared_state
        self.state = "Occam"

    def __str__(self):
        return self.state

class MyBorg(Borg):
    pass


if __name__ == '__main__':
    bg1 = Borg()
    bg2 = Borg()
    bg3 = Borg()

    bg1.state = 'Idle'
    bg2.state = 'Running'
    bg1.state = "Zombie"

    print (bg1)
    print (bg2)
