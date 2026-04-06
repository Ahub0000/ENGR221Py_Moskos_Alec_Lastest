import pytest

import os, sys 

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from myHashMap import MyHashMap

# Write your tests here

#i. put() tests 

def test_put_into_empty():
    my_map = MyHashMap()
    result = my_map.put("apple", 1)
    assert result == True
    assert my_map.get("apple") == 1

def test_put_nonempty_no_resize():
    my_map = MyHashMap()
    my_map.put("apple", 1)
    result = my_map.put("banana", 2)
    assert result == True
    assert my_map.get("banana") == 2

def test_put_triggers_resize():
    small_map = MyHashMap(load_factor=0.75, initial_capacity=4)
    small_map.put("a", 1)
    small_map.put("b", 2)
    small_map.put("c", 3)
    old_capacity = small_map.capacity
    small_map.put("d", 4) #triggers resize
    assert small_map.capacity == old_capacity * 2   

def test_put_duplicate_key():
    my_map = MyHashMap()
    my_map.put("apple", 1)
    result = my_map.put("apple", 99) #duplicate
    assert result == False
    assert my_map.get("apple") == 1 #value changed

# ii. replace() Tests
def test_replace_existing_key():
    my_map = MyHashMap()
    my_map.put("apple", 1)
    result = my_map.replace("apple", 100)
    assert result == True
    assert my_map.get("apple") == 100

def test_replace_missing_key():
    my_map = MyHashMap()
    result = my_map.replace("banana", 5)
    assert result == False

# iii. remove() tests

def test_replace_existing_key():
    my_map = MyHashMap()
    my_map.put("apple", 1)
    result = my_map.replace("apple")
    assert result == True
    assert my_map.get() == 0

def test_replace_missing_key():
    my_map = MyHashMap()
    result = my_map.replace("banana")
    assert result == False

# iv. set() Tests

def test_set_existing_key():
    my_map = MyHashMap()
    my_map.put("apple", 1)
    my_map.set("apple", 999)
    assert my_map.get("apple") == 999
    assert my_map.get_size() == 1    #size unchanged

def test_set_new_key():
    my_map = MyHashMap()
    my_map.set("cherry", 50)
    assert my_map.get("cherry") == 50
    assert my_map.get_size() == 1

# v. get() Tests

def test_get_existing_key():
    my_map = MyHashMap()
    my_map.put("apple", 42)
    assert my_map.get("apple") == 42

def test_get_missing_key():
    my_map = MyHashMap()
    assert my_map.get("banana") == None

# vi. size() tests

def test_size_empty():
    my_map = MyHashMap()
    assert my_map.get_size() == 0

def test_size_few_empty():
    my_map = MyHashMap()
    my_map.put("apple", 1)
    assert my_map.get_size() == 1

def test_size_few_empty():
    big_map = MyHashMap()
    for i in range(100):
        big_map.put(f"key{i}", i)
    assert big_map.get_size() == 100

#vii. isEmpty() Tests

def test_isEmpty_empty():
    my_map = MyHashMap()
    assert my_map.isEmpty() == True

def test_isEmpty_nonempty():
    my_map = MyHashMap()
    my_map.put("apple", 1)
    assert my_map.isEmpty() == False

# viii. containKey() tests

def test_containsKey_exists():
    my_map = MyHashMap()
    my_map.put("apple", 1)
    assert my_map.containsKey("apple") == True

def test_containsKey_missing():
    my_map = MyHashMap()
    assert my_map.containsKey("banana") == False

# ix. keys() tests

def test_keys_empty():
    my_map = MyHashMap()
    assert my_map.keys() == []

def test_keys_nonempty():
    my_map = MyHashMap()
    my_map.put("apple", 1)
    my_map.put("banana", 2)
    my_map.put("cherry", 3)
    assert sorted(my_map.keys()) == ["apple", "banana", "cherry "]

