import os, sys 

sys.path.append(os.path.dirname(__file__))

from myHashMap import MyHashMap
from entry import Entry

class Box:
    def __init__(self):
        self.nicknameMap = MyHashMap()
        self.populateBox()

    """
    Adds Entries to the Box from inputFile. Assume that each
    line in inputFile corresponds to an Entry."""
    def populateBox(self, inputFile='entries.txt'):
        # Open the file as read only
        with open(inputFile, 'r') as f:
            # Add each value in the file as an Entry to the Box
            for line in f:
                # Set the first word in the line as the nickname, and
                # the second as species
                nickname, species = line.split()
                # Add the new entry to the Box
                self.add(nickname, species)

    """
    Create an Entry object with the given information and add it
    to the nicknameMap. 
    Returns true if the Entry is successfully added to the Box, and
    false if the nickname already exists in the Box. """
    def add(self, nickname, species):
        
        if self.nicknameMap.containsKey(nickname):
            return False
        
        # Create a new Entry object and store it in the map
        # Key = nickname, Value = Entry object
        new_entry = Entry(nickname, species)
        self.nicknameMap.put(nickname, new_entry)
        return True

    """
    Return a single Entry object with the given nickname and species.
    Should not modify the Box itself. 
    Return None if the Entry does not exist in the Box. """
    def find(self, nickname, species):
        #Look up the entry by nickname
        entry = self.nicknameMap.get(self.nickname)

        #If it exists AND and species matches, return it
        if entry is not None and entry.getSpecies() == species:
            return entry
        
        #Otherwise return none
        return None

    """ 
    Return a list of nickanames representing all unique 
    nicknames in the Box. Should not modify the Box itself.
    Return None if the Box is empty. """
    def findAllNicknames(self):
        #If the box is empty, return None
        if self.nicknameMap.isEmpty():
            return None
        
        #Otherwise return all the keys (which are the nicknames)
        return self.nicknameMap.keys()

    """ 
    Return an Entry with the given nickname. Should not modify
    the Box itself. 
    Return None if the nickname is not in the Box. """
    def findEntryByNickname(self, nickname):
        #get () already returns None if the key doesn't exist
        return self.nicknameMap.get(nickname)

    """
    Remove the Entry with the given nickname from the Box. 
    Return true if successful, or false otherwise."""
    def removeByNickname(self, nickname):
        # remove() already returns True/False for us
        return self.nicknameMap.remove(nickname)

    """ 
    Remove the Entry with the given nickname and species. 
    Return true if successful, or false otherwise. """
    def removeEntry(self, nickname, species):
        #First check if the entry exists with that exact nickname AND species
        entry = self.find(nickname, species)

        #If it doesn't exist, return False
        if entry is None:
            return False
        
        #Otherwise remove it by nickname and return True
        return self.nicknameMap.remove(nickname)

if __name__ == '__main__':
    my_box = Box()

    #Test add
    print(my_box.add("Buddy", "Dog"))  #False 

    #Test find
    print(my_box.find("Buddy", "Dog"))  #Entry or none

    #Test findAllNicknames
    print(my_box.findAllNicknames()) #list of all nicknames

    #Test findEntryNicknames
    print(my_box.findEntryByNickname("Buddy"))  # Entry or None

     #Test findEntryNicknames
    print(my_box.removeByNickname("Buddy"))    # true or false

     #Test findEntryNicknames
    print(my_box.removeEntry("Buddy", "Dog"))  # true or false