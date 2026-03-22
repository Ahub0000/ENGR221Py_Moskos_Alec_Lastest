"""
Name: Alec Moskos
Lab 5
Description: This program implements a deque using a doubly linked list.
"""

import sys, os
sys.path.append(os.path.dirname(__file__))

from doubly_linked_list import DoublyLinkedList

class Deque():
    def __init__(self):
        self.__values = DoublyLinkedList()

    def is_empty(self):
        #check if deque is empty
        return self.__values.is_empty() 
    
    def __len__(self):
        #return number of items in deque
        return len(self.__values) 
    
    def __str__(self):
        #return string version of deque
        return str(self.__values) 

    def peek_left(self):
        #return leftmost value
        return self.__values.first() 

    def peek_right(self): 
        #retrun rightmost value
        return self.__values.get_last_node().get_value()

    def insert_left(self, value): 
        #insert at front
        self.__values.insert_front(value)
        
    def insert_right(self, value):  
        #insert at back
        self.__values.insert_back(value)

    def remove_left(self):  
        #remove and return front vlaue
        return self.__values.delete_first_node()

    def remove_right(self): 
        #return and return back value
        return self.__values.delete_last_node()

if __name__ == "__main__":
    pass