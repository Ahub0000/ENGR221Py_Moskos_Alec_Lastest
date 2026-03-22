"""
WRITE YOUR PROGRAM HEADER HERE
"""


import sys, os
sys.path.append(os.path.dirname(__file__))


from double_node import DoubleNode


class DoublyLinkedList():


    def __init__(self):
        self.__first_node = None
        self.__last_node = None


    def is_empty(self):
        return self.__first_node is None
   
    def get_first_node(self):
        return self.__first_node


    def get_last_node(self):
        return self.__last_node


    def first(self):
        if self.is_empty():
            raise Exception("Error: List is empty")
        return self.__first_node.get_value()
   
    def set_first_node(self, node):
        if type(node) != DoubleNode and node is not None:
            raise Exception("Error: Input must be a valid DoubleNode or None")
        self.__first_node = node


    def set_last_node(self, node):
        if type(node) != DoubleNode and node is not None:
            raise Exception("Error: Input must be a valid DoubleNode or None")
        self.__last_node = node




    def find(self, value):
        current = self.__first_node
        while current is not None:
            if current.get_value() == value:
                return current
            current = current.get_next_node()
        return None


    def insert_front(self, value):
        new_node = DoubleNode(value)


        if self.is_empty():
            self.__first_node=new_node
            self.__last_node=new_node
        else:
            new_node.set_next_node(self.get_first_node())
            self.get_first_node().set_previous_node(new_node)
            self.set_first_node(new_node)


    def insert_back(self, value):
        new_node = DoubleNode(value)
       
        if self.is_empty():
            self.set_first_node(new_node)
            self.set_last_node(new_node)
        else:
            new_node.set_previous_node(self.get_last_node())
            self.get_last_node().set_next_node(new_node)
            self.set_last_node(new_node)


    def insert_after(self, value_to_add, after_value):
        after_node = self.find(after_value)


        if after_node is None:
            return False
       
        new_node = DoubleNode(value_to_add)


        if after_node == self.__last_node:
            new_node.set_previous_node(after_node)
            after_node.set_next_node(new_node)
            self.set_last_node(new_node)
        else:
            next_node = after_node.get_next_node()
            new_node.set_previous_node(after_node)
            new_node.set_next_node(next_node)
            after_node.set_next_node(new_node)
            next_node.set_previous_node(new_node)
       
        return True


    def delete_first_node(self):
        if self.is_empty():
            raise Exception("Error: List is Empty")
       
        deleted_value = self.__first_node.get_value()


        if self.__first_node == self.__last_node:
            self.__first_node = None
            self.__last_node = None
        else:
            self.__first_node = self.__first_node.get_next_node()
            self.__first_node.set_previous_node(None)


        return deleted_value
   
    def delete_last_node(self):
        if self.is_empty():
            raise Exception("Error: List is Empty")
       
        deleted_value = self.__last_node.get_value()


        if self.__first_node == self.__last_node:
            self.__first_node = None
            self.__last_node = None
        else:
            self.__last_node = self.__last_node.get_previous_node()
            self.__last_node.set_next_node(None)


        return deleted_value
   
    def delete_value(self, value):
        if self.is_empty():
            raise Exception("Error: List is Empty")
       
        node_to_delete = self.find(value)


        if node_to_delete is None:
            return None
       
        if node_to_delete == self.__first_node:
            return self.delete_first_node()
       
        if node_to_delete == self.__last_node:
            return self.delete_last_node
       
        prev_node = node_to_delete.get_previous_node()
        next_node = node_to_delete.get_next_node()


        prev_node.set_next_node(next_node)
        next_node.set_previous_node(prev_node)


        return node_to_delete.get_value()


    def forward_traverse(self):
        current = self.__first_node
        while current is not None:
            print(current.get_value())
            current = current.get_next_node()


    def reverse_traverse(self):
        current = self.__last_node
        while current is not None:
            print(current.get_value())
            current = current.get_previous_node()


    def __len__(self):
        count = 0
        current = self.__first_node
        while current is not None:
            count +=1
            current = current.get_next_node()
        return count
   
    def __str__(self):
        values = []
        current = self.__first_node


        while current is not None:
            values.append(str(current.get_value()))
            current = current.get_next_node()
       
        return  "[" + " <-> ".join(values) + "]"
   
if __name__ == "__main__":
    pass
