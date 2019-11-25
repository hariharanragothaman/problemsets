"""
1. Create objects without having to specify the exact class
2. A factory is an object for creating other objects
"""

class TamilLocalizer:
    def __init__(self):
        self.translations = {"cat":"poonai", "frog":"thavalai"}

    def localize(self, msg):
        return self.translations.get(msg, msg)

class EnglishLocalizer:
    def localize(self, msg):
        return msg

def get_localizer(language="English"):
    """ 
    Factory
    Basically, returns an object of interest
    """
    localizers = {
            "English": EnglishLocalizer,
            "Tamil": TamilLocalizer, 
            }
    return localizers[language]()

if __name__ == '__main__':
    e = get_localizer()
    t = get_localizer(language='Tamil')
    print (e)
    print (t)
