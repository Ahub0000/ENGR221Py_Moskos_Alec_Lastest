import pytest

import os, sys 

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from binarySearchTree import BinarySearchTree

@pytest.fixture 
# Define an empty BST for testing
def emptyTree():
    return BinarySearchTree()

@pytest.fixture 
# Define a BST for testing
# Should look like
#          5
#        /   \
#       3     8
#      /
#     1
def nonemptyTree():
    bst = BinarySearchTree()
    bst.insert(5, "five")
    bst.insert(8, "eight")
    bst.insert(3, "three")
    bst.insert(1, "one")
    return bst

####
# isEmpty
####

@pytest.mark.isEmpty
# isEmpty functionality for a BST
def test_bst_isempty_true(emptyTree):
    # Should return True
    assert emptyTree.isEmpty()

@pytest.mark.isEmpty
# isEmpty functionality for a BST
def test_bst_isempty_false(nonemptyTree):
    # Should return False 
    assert not nonemptyTree.isEmpty()

####
# getRoot
####

@pytest.mark.getRoot
# getRoot functionality for a BST
def test_bst_getRoot_empty(emptyTree):
    # Should be None
    assert emptyTree.getRoot() is None 

@pytest.mark.getRoot
# getRoot functionality for a BST
def test_bst_getRoot_nonempty(nonemptyTree):
    # Should return 5
    assert nonemptyTree.getRoot().key == 5

####
# search
####

@pytest.mark.search
# search functionality for a BST
def test_bst_search_present(nonemptyTree):
    # Should return 3
    assert nonemptyTree.search(3).key == 3

@pytest.mark.search
# search functionality for a BST
def test_bst_search_absent(nonemptyTree):
    # Should return None
    assert nonemptyTree.search(4) is None

####
# lookup
####

@pytest.mark.lookup
# lookup functionality for a BST
def test_bst_lookup_present(nonemptyTree):
    # Should return "one"
    assert nonemptyTree.lookup(1) == "one"

@pytest.mark.lookup
# lookup functionality for a BST
def test_bst_lookup_present(nonemptyTree):
    try:
        # This should throw an exception
        nonemptyTree.lookup(4)
    except:
        # If we got here, an exception was thrown
        assert True 

####
# findSuccessor
####

@pytest.mark.findSuccessor
# findSuccessor functionality for a BST
def test_bst_findSuccessor(nonemptyTree):
    # Should return smallest value in tree (1)
    assert nonemptyTree.findSuccessor(nonemptyTree.getRoot()).key == 1

####
# delete
####

@pytest.mark.delete
# delete functionality for a BST
def test_bst_delete_leaf(nonemptyTree, capfd):
    # Delete a leaf
    nonemptyTree.delete(1)
    # Print the tree
    print(nonemptyTree)
    # Capture the output
    out, _ = capfd.readouterr()
    # Confirm that the output has 1 removed
    assert out == "{(5, five), {(3, three), None, None}, {(8, eight), None, None}}\n"

@pytest.mark.delete
# delete functionality for a BST
def test_bst_delete_child(nonemptyTree, capfd):
    # Delete a node with one child
    nonemptyTree.delete(3)
    # Print the tree
    print(nonemptyTree)
    # Capture the output
    out, _ = capfd.readouterr()
    # Confirm that the output has 3 removed
    assert out == "{(5, five), {(1, one), None, None}, {(8, eight), None, None}}\n"

@pytest.mark.delete
# delete functionality for a BST
def test_bst_delete_children(nonemptyTree, capfd):
    # Delete a node with two children
    nonemptyTree.delete(5)
    # Print the tree
    print(nonemptyTree)
    # Capture the output
    out, _ = capfd.readouterr()
    # Confirm that the output has 5 removed
    assert out == "{(8, eight), {(3, three), {(1, one), None, None}, None}, None}\n"

@pytest.mark.delete
# delete functionality for a BST
def test_bst_delete_stick(nonemptyTree, capfd):
    # Delete so we are left with a stick
    nonemptyTree.delete(5)
    # Now delete so we are forced to change the root in Case 2
    nonemptyTree.delete(8)
    # Print the tree
    print(nonemptyTree)
    # Capture the output
    out, _ = capfd.readouterr()
    # Confirm that the output has 5 removed
    assert out == "{(3, three), {(1, one), None, None}, None}\n"
    
@pytest.mark.traverse
# traverse functionality for a BST
def test_bst_traverse(nonemptyTree, capfd):
    # Traverse the tree
    nonemptyTree.traverse()
    # Capture the output
    out, _ = capfd.readouterr()
    # Confirm that the output is in the expected order
    assert out == "(1, one)\n(3, three)\n(5, five)\n(8, eight)\n"