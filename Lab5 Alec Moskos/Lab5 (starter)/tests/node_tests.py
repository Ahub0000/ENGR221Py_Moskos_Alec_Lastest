import pytest

import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from double_node import DoubleNode

@pytest.fixture 
# Define a DoubleNode for testing
def node(value=5):
    return DoubleNode(value)

####
# is_first
####

@pytest.mark.is_first
# is_first functionality for DoubleNode
def test_doublenode_isfirst_true(node):
    # is_first should return True
    assert node.is_first()

@pytest.mark.is_first
# is_first functionality for DoubleNode
def test_doublenode_isfirst_false(node):
    # Create a new DoubleNode and set previous
    dn2 = DoubleNode(3, next=None, previous=node)
    # is_first should return False
    assert not dn2.is_first()

####
# is_last
####

@pytest.mark.is_last
# is_last functionality for DoubleNode
def test_doublenode_islast_true(node):
    # is_last should return True
    assert node.is_last()

@pytest.mark.is_last
# is_last functionality for DoubleNode
def test_doublenode_islast_false(node):
    # Create a new DoubleNode and set next
    dn2 = DoubleNode(3, next=node, previous=None)
    # is_last should return False
    assert not dn2.is_last()

####
# get_falue
####

@pytest.mark.get_value
# get_value functionality for DoubleNode
def test_doublenode_get_value(node):
    # node has value 5 by default
    assert node.get_value() == 5

####
# get_next_node
####

@pytest.mark.get_next_node
# get_next_node functionality for DoubleNode
def test_doublenode_get_next_node(node):
    # Create a new DoubleNode and set next
    dn2 = DoubleNode(3, next=node, previous=None)
    # Check that dn2's next node was set correctly
    assert dn2.get_next_node() == node

####
# get_previous_node
####

@pytest.mark.get_previous_node
# get_previous_node functionality for DoubleNode
def test_doublenode_get_previous_node(node):
    # Create a new DoubleNode and set previous
    dn2 = DoubleNode(3, next=None, previous=node)
    # Check that dn2's previous node was set correctly
    assert dn2.get_previous_node() == node

####
# set_value
####

@pytest.mark.set_value
# set_value functionality for DoubleNode
def test_doublenode_set_value(node):
    # Change node's value to 3
    node.set_value(3)
    # Check that the new value is correct
    assert node.get_value() == 3

####
# set_next_node
####

@pytest.mark.set_next_node
# set_next_node functionality for DoubleNode 
def test_doublenode_set_next_node(node):
    # Create a new doubleNode
    dn2 = DoubleNode(3)
    # Set node's next to dn2
    node.set_next_node(dn2)
    # Check that the next node was set correctly
    assert node.get_next_node() == dn2 

####
# set_previous_node
####

@pytest.mark.set_previous_node
# set_previous_node functionality for DoubleNode 
def test_doublenode_set_previous_node(node):
    # Create a new doubleNode
    dn2 = DoubleNode(3)
    # Set node's previous to dn2
    node.set_previous_node(dn2)
    # Check that the previous node was set correctly
    assert node.get_previous_node() == dn2 

####
# __str__
####

@pytest.mark.str
# __str__ functionality for DoubleNode
def test_doublenode_str(node, capfd):
    # Print the node
    print(node)
    # Capture the output
    out, _ = capfd.readouterr()
    # Confirm that the output is as expected
    assert out == "5\n"