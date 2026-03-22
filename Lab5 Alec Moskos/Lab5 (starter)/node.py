"""
node.py
Represents a Node in a singly linked list
"""

class Node():

    def __init__(self, value, next=None):
        self.__value = value    # The value of the node
        self.__next_node = next  # The next node in the list

    ###########
    # Methods #
    ###########

    # Return whether the given node is the first in the list
    def is_first(self):
        return self.__next_node == None

    #####
    # Getters
    #####
        
    # Return the value of the node
    def get_value(self):
        return self.__value 
    
    # Return the next node in the list
    def get_next_node(self):
        return self.__next_node
    
    #####
    # Setters
    #####

    # Set the value of the node to a new value
    def set_value(self, new_value):
        self.__value = new_value 

    # Set the next node to a new node
    def set_next_node(self, new_next):
        # Confirm that the input is a valid node
        if self.__check_valid_node(new_next):
            self.__next_node = new_next 

    #####
    # Helpers
    #####

    # Check whether the input node is a valid Node or None
    # Return True if it is, or raise an exception if not
    def __check_valid_node(self, node):
        if type(node) != Node and node != None:
            raise Exception("Error: Input must be a valid Node or None")
        return True
    
    # This overloads the built in __str__ method and will
    # be run when printing a node (e.g., print(node))
    def __str__(self):
        return str(self.get_value())
    
if __name__ == "__main__":
    pass