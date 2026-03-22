import pytest

import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from deque import Deque 

@pytest.fixture 
# Define an empty Deque for testing
def empty_deque():
    return Deque()

@pytest.fixture 
# Define a Deque for testing
# Should look like [3 <-> 2 <-> 1]
def nonempty_deque():
    d = Deque()
    d.insert_left(1)
    d.insert_left(2)
    d.insert_left(3)
    return d

####
# is_empty
####

@pytest.mark.is_empty 
# is_empty functionality for a Deque
def test_deque_is_empty_true(empty_deque):
    # is_empty should return True
    assert empty_deque.is_empty()

@pytest.mark.is_empty 
# is_empty functionality for a Deque
def test_deque_is_empty_false(nonempty_deque):
    # is_empty should return False
    assert not nonempty_deque.is_empty()

####
# __len__
####

@pytest.mark.len
# __len__ functionality for a Deque
def test_deque_len(nonempty_deque):
    # Check that the len of the deque is correct
    assert len(nonempty_deque) == 3

####
# __str__
####

@pytest.mark.str
# __str__ functionality for a Deque
def test_deque_str(nonempty_deque, capfd):
    # Print the deque
    print(nonempty_deque)
    # Capture the output
    out, _ = capfd.readouterr()
    # Confirm that the output is in the expected format
    assert out == "[3 <-> 2 <-> 1]\n"

####
# peek_left
####

@pytest.mark.peek_left
# peek_left functionality for a Deque
def test_deque_peek_left(nonempty_deque):
    # Check that we are checking the first (leftmost) node
    assert nonempty_deque.peek_left() == 3

####
# peek_right
####

@pytest.mark.peek_right
# peek_right functionality for a Deque
def test_deque_peek_right(nonempty_deque):
    # Check that we are checking the last (rightmost) node
    assert nonempty_deque.peek_right() == 1

####
# insert_left
####

@pytest.mark.insert_left
# insert_left functionality for a Deque
def test_deque_insert_left_len(nonempty_deque):
    # Insert an item to the left of the deque
    nonempty_deque.insert_left(4)
    # Check that the deque has an additional item
    assert len(nonempty_deque) == 4

@pytest.mark.insert_left
# insert_left functionality for a Deque
def test_deque_insert_left_value(nonempty_deque):
    # Insert an item to the left of the deque
    nonempty_deque.insert_left(4)
    # Check that the deque has an additional item
    assert nonempty_deque.peek_left() == 4

####
# insert_right
####

@pytest.mark.insert_right
# insert_right functionality for a Deque
def test_deque_insert_right_len(nonempty_deque):
    # Insert an item to the right of the deque
    nonempty_deque.insert_right(4)
    # Check that the deque has an additional item
    assert len(nonempty_deque) == 4

@pytest.mark.insert_right
# insert_right functionality for a Deque
def test_deque_insert_right_value(nonempty_deque):
    # Insert an item to the right of the deque
    nonempty_deque.insert_right(4)
    # Check that the deque has an additional item
    assert nonempty_deque.peek_right() == 4

####
# remove_left
####

@pytest.mark.remove_left
# remove_left functionality for a Deque
def test_deque_remove_left_len(nonempty_deque):
    # Remove an item from the left of the deque
    nonempty_deque.remove_left()
    # Check that the deque has one less item
    assert len(nonempty_deque) == 2

@pytest.mark.remove_left
# remove_left functionality for a Deque
def test_deque_remove_left_val(nonempty_deque):
    # Remove an item from the left of the deque
    val = nonempty_deque.remove_left()
    # Check that the removed value was as expected
    assert val == 3

####
# remove_right
####

@pytest.mark.remove_right
# remove_right functionality for a Deque
def test_deque_remove_right_len(nonempty_deque):
    # Remove an item from the right of the deque
    nonempty_deque.remove_right()
    # Check that the deque has one less item
    assert len(nonempty_deque) == 2

@pytest.mark.remove_right
# remove_right functionality for a Deque
def test_deque_remove_right_val(nonempty_deque):
    # Remove an item from the right of the deque
    val = nonempty_deque.remove_right()
    # Check that the removed value was as expected
    assert val == 1