#Singleton Design Pattern

class ConfigValues:

    __instance = None

    @staticmethod
    def getinstance():
        if ConfigValues.__instance == None:
            ConfigValues()
        return ConfigValues.__instance
    
    def __init__(self):
        """ Virtually private constructor. """
        if ConfigValues.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            ConfigValues.__instance = self



s = ConfigValues.getinstance()
print(s)

s = ConfigValues.getinstance()
print(s)

s = ConfigValues()
print(s)

