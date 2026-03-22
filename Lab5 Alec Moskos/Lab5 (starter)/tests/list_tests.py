import pytest

import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from doubly_linked_list import DoublyLinkedList
from double_node import DoubleNode

@pytest.fixture 
# Define an empty DoublyLinkedList for testing
def empty_list():
    return DoublyLinkedList()

@pytest.fixture 
# Define a DoublyLinkedList for testing
# Should look like [3 <-> 2 <-> 1]
def nonempty_list():
    dll = DoublyLinkedList()
    dll.insert_front(1)
    dll.insert_front(2)
    dll.insert_front(3)
    return dll

####
# is_empty
####

@pytest.mark.is_empty
# is_empty functionality for a DoublyLinkedList
def test_dll_is_empty_true(empty_list):
    # Should return True
    assert empty_list.is_empty()

@pytest.mark.is_empty
# is_empty functionality for a DoublyLinkedList
def test_dll_is_empty_false(nonempty_list):
    # Should return False 
    assert not nonempty_list.is_empty()

####
# first
####

@pytest.mark.first
# first functionality for a DoublyLinkedList
def test_dll_first(nonempty_list):
    # Check that first returns the value of the first (leftmost) item
    assert nonempty_list.first() == 3

####
# set_first_node
####

@pytest.mark.set_first_node
# set_first_node functionality for a DoublyLinkedList
def test_dll_set_first_node(nonempty_list):
    # Create a new node
    dn = DoubleNode(4)
    # Set the new node as the first node of the list
    nonempty_list.set_first_node(dn)
    # Check that get_first_node returns the newly set first node
    assert nonempty_list.get_first_node() == dn

@pytest.mark.set_first_node
# set_first_node functionality for a DoublyLinkedList
def test_dll_set_first_node_invalid(nonempty_list):
    # Try to set the first node of the list to an integer
    try:
        nonempty_list.set_first_node(4)
        # The above line should have thrown an exception,
        # so this assert should not run
        assert False
    except:
        # Successfully threw an exception
        assert True

####
# set_last_node
####

@pytest.mark.set_last_node
# set_last_node functionality for a DoublyLinkedList
def test_dll_set_last_node(nonempty_list):
    # Create a new node
    dn = DoubleNode(4)
    # Set the new node as the last node of the list
    nonempty_list.set_last_node(dn)
    # Check that get_last_node returns the newly set last node
    assert nonempty_list.get_last_node() == dn

@pytest.mark.set_last_node
# set_last_node functionality for a DoublyLinkedList
def test_dll_set_last_node_invalid(nonempty_list):
    # Try to set the last node of the list to an integer
    try:
        nonempty_list.set_last_node(4)
        # The above line should have thrown an exception,
        # so this assert should not run
        assert False
    except:
        # Successfully threw an exception
        assert True

####
# find
####

@pytest.mark.find 
# find functionality for a DoublyLinkedList
def test_dll_find(nonempty_list):
    # 1 is the last (rightmost) element of nonempty_list
    assert nonempty_list.find(1) == nonempty_list.get_last_node()

@pytest.mark.find 
# find functionality for a DoublyLinkedList
def test_dll_find_notpresent(empty_list):
    # 1 is not in the empty list
    assert empty_list.find(1) == None

####
# insert_front
####

@pytest.mark.insert_front
# insert_front functionality for an empty DoublyLinkedList 
def test_dll_insert_front_empty_first(empty_list):
    # Insert a new value to the list
    empty_list.insert_front(5)
    # Check that the inserted value was set as the list's
    # first node
    assert empty_list.get_first_node().get_value() == 5

@pytest.mark.insert_front
# insert_front functionality for an empty DoublyLinkedList 
def test_dll_insert_front_empty_last(empty_list):
    # Insert a new value to the list
    empty_list.insert_front(5)
    # Check that the inserted value was set as the list's
    # last node
    assert empty_list.get_last_node().get_value() == 5

@pytest.mark.insert_front
# insert_front functionality for a DoublyLinkedList 
def test_dll_insert_front_nonempty_first(nonempty_list):
    # Insert a new value to the list
    nonempty_list.insert_front(5)
    # Check that the inserted value was set as the list's
    # first node
    assert nonempty_list.get_first_node().get_value() == 5

@pytest.mark.insert_front
# insert_front functionality for a DoublyLinkedList 
def test_dll_insert_front_nonempty_last(empty_list):
    # Insert a new value to the list
    empty_list.insert_front(2)
    # Insert a new value to the list
    empty_list.insert_front(1)
    # Check that the inserted value was set as the next
    # node's previous node
    assert empty_list.get_last_node().get_previous_node().get_value() == 1

####
# insert_back
####

@pytest.mark.insert_back
# insert_back functionality for an empty DoublyLinkedList 
def test_dll_insert_back_empty_last(empty_list):
    # Insert a new value to the list
    empty_list.insert_back(5)
    # Check that the inserted value was set as the list's
    # last node
    assert empty_list.get_last_node().get_value() == 5

@pytest.mark.insert_back
# insert_back functionality for an empty DoublyLinkedList 
def test_dll_insert_back_empty_first(empty_list):
    # Insert a new value to the list
    empty_list.insert_back(5)
    # Check that the inserted value was set as the list's
    # first node
    assert empty_list.get_first_node().get_value() == 5

@pytest.mark.insert_back
# insert_back functionality for a DoublyLinkedList 
def test_dll_insert_back_nonempty_last(nonempty_list):
    # Insert a new value to the list
    nonempty_list.insert_back(5)
    # Check that the inserted value was set as the list's
    # last node
    assert nonempty_list.get_last_node().get_value() == 5

@pytest.mark.insert_back
# insert_back functionality for a DoublyLinkedList 
def test_dll_insert_back_nonempty_first(empty_list):
    # Insert a new value to the list
    empty_list.insert_back(2)
    # Insert a new value to the list
    empty_list.insert_back(1)
    # Check that the inserted value was set as the previous
    # node's next node
    assert empty_list.get_first_node().get_next_node().get_value() == 1

@pytest.mark.insert_back
# insert_back functionality for a DoublyLinkedList
def test_dll_insert_back_nonempty_previous(nonempty_list):
    # Insert a new value to the list
    nonempty_list.insert_back(5)
    # Check that the inserted node's previous node was set
    # to the correct node
    assert nonempty_list.get_last_node().get_previous_node().get_value() == 1

####
# insert_after
####

@pytest.mark.insert_after
# insert_after functionality for a DoublyLinkedList
def test_dll_insert_after_last(nonempty_list):
    # Insert a new value to the end of the list
    nonempty_list.insert_after(4, 1)
    # Check that the inserted value was set as the last
    # node in the list
    assert nonempty_list.get_last_node().get_value() == 4

@pytest.mark.insert_after
# insert_after functionality for a DoublyLinkedList
def test_dll_insert_after_notlast_prevnext(nonempty_list):
    # Insert a new value as the second element of the list
    nonempty_list.insert_after(4, 3)
    # Check that the inserted node was set as the next node for
    # the previous one
    assert nonempty_list.get_first_node().get_next_node().get_value() == 4

@pytest.mark.insert_after
# insert_after functionality for a DoublyLinkedList
def test_dll_insert_after_notlast_next(nonempty_list):
    # Insert a new value as the second element of the list
    nonempty_list.insert_after(4, 3)
    # Check that the inserted value's next node was set to
    # the node after
    assert nonempty_list.get_first_node().get_next_node().get_next_node().get_value() == 2

@pytest.mark.insert_after
# insert_after functionality for a DoublyLinkedList
def test_dll_insert_after_notlast_previous(nonempty_list):
    # Insert a new value as the second element of the list
    nonempty_list.insert_after(4, 3)
    # Check that the inserted value's previous node was set to
    # the correct value
    assert nonempty_list.get_first_node().get_next_node().get_previous_node().get_value() == 3

@pytest.mark.insert_after
# insert_after functionality for a DoublyLinkedList
def test_dll_insert_after_notlast_nextprev(nonempty_list):
    # Insert a new value as the second element of the list
    nonempty_list.insert_after(4, 3)
    # Check that the inserted node was set as the previous node
    # for the next node
    assert nonempty_list.get_first_node().get_next_node().get_next_node().get_previous_node().get_value() == 4

####
# delete_first_node
####

@pytest.mark.delete_first_node
# delete_first_node functionality for a DoublyLinkedList
def test_dll_delete_first_node_oneitem_val(empty_list):
    # Insert a new node to the list
    empty_list.insert_front(1)
    # Delete the inserted node
    val = empty_list.delete_first_node()
    # Check that the value of the deleted node is as expected
    assert val == 1

@pytest.mark.delete_first_node
def test_dll_delete_first_node_oneitem_first(empty_list):
    # Insert a new node to the list
    empty_list.insert_front(1)
    # Delete the inserted node
    empty_list.delete_first_node()
    # Check that the first node of the list was set to None
    assert empty_list.get_first_node() == None

@pytest.mark.delete_first_node
def test_dll_delete_first_node_prev(nonempty_list):
    # Delete the first
    nonempty_list.delete_first_node()
    # Check that the next node's previous was set to None
    assert nonempty_list.get_first_node().get_previous_node() == None

@pytest.mark.delete_first_node
def test_dll_delete_first_node_first(nonempty_list):
    # Delete the first
    nonempty_list.delete_first_node()
    # Check that the first node of the list was set to the next one
    assert nonempty_list.get_first_node().get_value() == 2

####
# delete_last_node
####
    
@pytest.mark.delete_last_node
# delete_last_node functionality for a DoublyLinkedList
def test_dll_delete_last_node_oneitem_val(empty_list):
    # Insert a new node to the list
    empty_list.insert_front(1)
    # Delete the inserted node
    val = empty_list.delete_last_node()
    # Check that the value of the deleted node is as expected
    assert val == 1

@pytest.mark.delete_last_node
# delete_last_node functionality for a DoublyLinkedList
def test_dll_delete_last_node_oneitem_last(empty_list):
    # Insert a new node to the list
    empty_list.insert_front(1)
    # Delete the inserted node
    val = empty_list.delete_last_node()
    # Check that the last node of the list was set to None
    assert empty_list.get_last_node() == None

@pytest.mark.delete_first_node
def test_dll_delete_last_node_prev(nonempty_list):
    # Delete the last node
    nonempty_list.delete_last_node()
    # Check that the previous node's next was set to None
    assert nonempty_list.get_last_node().get_next_node() == None

@pytest.mark.delete_last_node
def test_dll_delete_last_node_first(nonempty_list):
    # Delete the last
    nonempty_list.delete_last_node()
    # Check that the last node of the list was set to the previous one
    assert nonempty_list.get_last_node().get_value() == 2

####
# delete_value
####
    
@pytest.mark.delete_value
# delete_value functionality for a DoublyLinkedList
def test_dll_delete_value_val(nonempty_list):
    # Delete the value from the list
    val = nonempty_list.delete_value(2)
    # Check that the value of the deleted node is as expected
    assert val == 2

@pytest.mark.delete_value
# delete_value functionality for a DoublyLinkedList
def test_dll_delete_value_next(nonempty_list):
    # Delete the value from the list
    nonempty_list.delete_value(2)
    # Check that the previous node's next node was set
    # as expected
    assert nonempty_list.get_first_node().get_next_node().get_value() == 1

@pytest.mark.delete_value
# delete_value functionality for a DoublyLinkedList
def test_dll_delete_value_prev(nonempty_list):
    # Delete the value from the list
    nonempty_list.delete_value(2)
    # Check that the next node's previous node was set
    # as expected
    assert nonempty_list.get_last_node().get_previous_node().get_value() == 3

####
# forward_traverse
####

@pytest.mark.forward_traverse
# forward_traverse functionality for a DoublyLinkedList
def test_dll_forward_traverse(nonempty_list, capfd):
    # Print each item in the list
    nonempty_list.forward_traverse()
    # Capture the output
    out, _ = capfd.readouterr()
    # Confirm that the output matches what is expected
    assert out == "3\n2\n1\n"

####
# reverse_traverse
####

@pytest.mark.reverse_traverse
# reverse_traverse functionality for a DoublyLinkedList
def test_dll_reverse_traverse(nonempty_list, capfd):
    # Print each item in the list in reverse order
    nonempty_list.reverse_traverse()
    # Capture the output
    out, _ = capfd.readouterr()
    # Confirm that the output matches what is expected
    assert out == "1\n2\n3\n"

####
# __len__
####

@pytest.mark.len
# __len__ functionality for a DoublyLinkedList
def test_dll_len(nonempty_list):
    # Check that the len of the list is correct
    assert len(nonempty_list) == 3

####
# __str__
####

@pytest.mark.str
# __str__ functionality for a DoublyLinkedList
def test_dll_str(nonempty_list, capfd):
    # Print the list
    print(nonempty_list)
    # Capture the output
    out, _ = capfd.readouterr()
    # Confirm that the output is in the expected format
    assert out == "[3 <-> 2 <-> 1]\n"