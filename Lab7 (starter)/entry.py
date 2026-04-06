class Entry():
    def __init__(self, nickname, species):
        self.__nickname = nickname
        self.__species = species

    def __str__(self):
        return "Nickname: {}, Species: {}".format(self.__nickname, self.__species)
    
    # Returns the nickname of this entry
    def getNickname(self):
        return self.__nickname
    
    # Returns the species of this entry
    def getSpecies(self):
        return self.__species