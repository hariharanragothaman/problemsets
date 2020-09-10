"""
Pattern Type: Creational Pattern
This pattern restricts the instantiation of a class to one object.

Involves one class to create methods and specified objects
"""

class Singleton:
    __instance = None

    @staticmethod
    def getInstance():
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance

    def __init__(self):
        """
        Virtually Private Constructor
        """
        if Singleton.__instance != None:
            raise Exception("This class is a singleton")
        else:
            Singleton.__instance = self


if __name__ == '__main__':
    s = Singleton()
    print (s)
    a = Singleton.getInstance()
    print (a)
