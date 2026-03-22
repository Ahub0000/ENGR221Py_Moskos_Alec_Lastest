"""
linkedList.py
Implementation of a singly linked list
"""

import sys, os
sys.path.append(os.path.dirname(__file__))

from node import Node 

class LinkedList():
    
    def __init__(self):
        self.__first_node = None # The first node in the list

    ###########
    # Methods #
    ###########
        
    # Return whether or not the list is empty
    def is_empty(self):
        return self.get_first_node() == None

    # Return the first node in the list
    def get_first_node(self):
        return self.__first_node
    
    # Return the value of the first node in the list
    def first(self):
        # Raise an exception if the list is empty
        if self.is_empty():
            raise Exception("Error: List is empty, cannot return first  value")
        return self.get_first_node().get_value()
    
    # Set the first node of the list to a new node
    def set_first_node(self, node):
        # Raise an exception if the input is not a valid node
        if node != None and type(node) != Node:
            raise Exception("Error: Input must be valid Node or None")
        else:
            self.__first_node = node 
    
    # Return the node containing the given value in the list.
    # If the value is not in the list, return None.
    def find(self, value):
        # Traverse down the list, starting with the first node
        node = self.get_first_node()
        while node != None:
            # If this node has the given value, return it
            if node.get_value() == value:
                return node 
            # Otherwise, grab the next node to check
            node = node.get_next_node()
        # If the value was not found, return None
        return None

    # Insert the given value to the front of the list
    def insert(self, value):
        # Create a new node that points to the first node in the list
        node = Node(value, self.get_first_node())
        # Set the new node to be the first in the list
        self.set_first_node(node)

    # Insert the given value_to_add into the list after after_value.
    # Return True if inserted successfully, or False if after_value
    # is not found in the list.
    def insert_after(self, value_to_add, after_value):
        # Find the node with value after_value
        node = self.find(after_value)
        # If the value was not found, return False
        if node == None:
            return False 
        # Otherwise, create a new node with value_to_add that
        # points to the node after the one with after_value
        new_node = Node(value_to_add, node.get_next_node())
        # Set after_value's next node to be the new node
        node.set_next_node(new_node)
        # Return True that the item was inserted successfully
        return True
    
    # Delete the first node from the list and return the value
    # of the node that was deleted
    def delete_first_node(self):
        # If we try to delete from an empty list, raise an exception
        if self.is_empty():
            raise Exception("Error: List is empty")
        # Otherwise, grab the first node of the list
        first = self.get_first_node()
        # Set the first node of the list to the second node
        self.set_first_node(first.get_next_node())
        # Return the value of the deleted node
        return first.get_value()
    
    # Delete an item with the given value from the list and return
    # True if the value was deleted, or None if it failed.
    def delete_value(self, value):
        # If we try to delete from an empty list, raise an exception
        if self.is_empty():
            raise Exception("Error: Cannot delete from empty list")
        # Otherwise, traverse down the list starting with the first node
        previous = self.get_first_node()
        while previous.get_next_node() != None:
            # Get the next node in the list
            next = previous.get_next_node() 
            # Check whether we want to delete the next node
            if value == next.get_value():
                # If so, change the next node of the previous node
                # to be the next node of the one we are deleting
                previous.set_next_node(next.get_next_node())
                # Return that the value was deleted
                return True
            # Update previous to be the next item in the list
            previous = next 
        # If the value was not found, raise an exception
        raise Exception("Error: Cannot find value {} in list".format(value))

    # Print each item in the list from beginning to end
    def traverse(self):
        # Traverse starting from the first node
        node = self.get_first_node()
        # Stop when we reach the end of the list
        while node != None:
            # Print the value of this node
            print(node.get_value())
            # Update node to be the next node
            node = node.get_next_node()

    # This overloads the built in __len__ method and will be run
    # when checking the length of a linkedList (e.g., len(linkedList))
    def __len__(self):
        # A counter starting at 0
        l = 0
        # Traverse down the list starting with the first node
        node = self.get_first_node() 
        # Stop when we reach the end of the list
        while node != None:
            # Increment the counter for each node we find
            l += 1
            # Update node to be the next node
            node = node.get_next_node()
        # Return the counter
        return l 
    
    # This overloads the built in __str__ method and will be 
    # run when printing a linked list (e.g., print(linkedList)).
    # Outputs the list in format "[val1 > val2 > ... > valn]"
    def __str__(self):
        # Begin the string with the left bracket
        out = "["
        # Traverse down the list starting with the first node
        node = self.get_first_node() 
        # Stop when we reach the end of the list
        while node != None:
            # Only add the arrow if there's more than one value in the list
            if len(out) > 1:
                out += " > "
            # Add the value of the current node to the string
            out += str(node)
            # Update node to be the next node
            node = node.get_next_node()
        # Add the closing bracket and return the string
        return out + "]"
    
if __name__ == "__main__":
    pass