"""
WRITE YOUR PROGRAM HEADER HERE
"""

class DoubleNode():

    def __init__(self, value, next=None, previous=None):
        self.__value = value
        self.__next_node = next
        self.__previous_node = previous 

    #####
    # Methods
    #####
        
    def is_first(self):
        return self.__previous_node is None
        
    def is_last(self):
        return self.__next_node is None

    #####
    # Getters
    #####

    def get_value(self):
        return self.__value
    
    def get_next_node(self):
        return self.__next_node

    def get_previous_node(self):
        return self.__previous_node

    #####
    # Setters
    #####

    def set_value(self, new_value):
        self.__value = new_value

    def set_next_node(self, new_next):
        self.__check_valid_node = (new_next)
        self.__next_node = new_next

    def set_previous_node(self, new_previous):
        self.__check_valid_node = (new_previous)
        self.__previous_node = new_previous

    #####
    # Helpers
    #####

    def __check_valid_node(self, node):
        if type(node) != DoubleNode and node != None:
            raise Exception("Error: Input must be a valid DoubleNode or None")
        return True
    
    def __str__(self):
        return str(self.__value)

if __name__ == "__main__":
    pass