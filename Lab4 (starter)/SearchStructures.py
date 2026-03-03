"""
WRITE YOUR PROGRAM HEADER HERE
"""

# Implementation of a Stack
class Stack():
    def __init__(self):
        self.items = []

    # Returns True if the Stack is empty, or False if it is not empty
    def isEmpty(self):
        #If length is 0, it is empty
        if len(self.items) == 0:    
            return True
        else:
            return False
    
    # For a Stack, this should "push" item to the top of the Stack
    #Add items to the top of the stack
    def add(self, item):
        #apped adds the items to the end of the list
        #the end of the list is the top of the stack
        self.items.append(item)

    # For a Stack, this should "pop" an item from the Stack
    # and return it
    def remove(self):
        #First check if stack is empty
        if self.isEmpty():
            return None
        
        #Get the last item (top of the stack)
        top_item = self.items[-1]

        #Remove the last item by slicing off the end
        self.items = self.items[:-1]

        #pop removes the last item
        return top_item

#Queue (First In, First Out) 
# Implementation of a Queue
class Queue():
    def __init__(self):
        self.items = []     # list to store queue items

    # Returns True if the Queue is empty, or False if it is not empty
    def isEmpty(self):
        return self.items == []

    # For a Queue, this should "enqueue" item to the end of the Queue
    def add(self, item):
        self.items.append(item) #add to back

    # For a Queue, this should "dequeue" an item from the Queue
    # and return it
    def remove(self):
        if self.isEmpty():
            return None
        
        #Get the first item (Front of queue)
        front_item = self.items[0]

        #Remove the first item
        self.items = self.items[1:]

        return front_item