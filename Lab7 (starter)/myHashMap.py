"""
WRITE YOUR PROGRAM HEADER HERE

Adapted from UCSD CSE12
"""

class MyHashMap:
    def __init__(self, load_factor=0.75,
                       initial_capacity=16):
        self.load_factor = load_factor 
        self.capacity = initial_capacity 
        self.size = 0
        self.buckets = [[] for _ in range(self.capacity)]

    """
    Resizes the self.buckets array when the load_factor is reached. """
    def resize(self):
        # Double the number of buckets
        self.capacity *= 2 
        # Make a copy of the current contents in the buckets
        old_buckets = self.buckets 
        # Create a new set of buckets that's twice as big as the old one
        self.buckets = [[] for _ in range(self.capacity)]
        # Add each key, value pair already in the MyHashMap to the new buckets
        for bucket in old_buckets:
            if bucket != []:
                for entry in bucket:
                    self.put(entry.getKey(), entry.getValue())

    def get_bucket_index(self, key):
        return abs(hash(key))  % self.capacity

    """
    Adds the specified key, value pair to the MyHashMap if 
    the key is not already in the MyHashMap. If adding a new key would
    surpass the load_factor, resize the MyHashMap before adding the key.
    Return true if successfully added to the MyHashMap.
    Raise an exception if the key is None. """
    def put(self, key, value):
        if key is None:
            raise Exception("Key cannot be None")
        
        #Resize if needed beofre adding
        if (self.size + 1) / self.capacity > self.load_factor:
            self.resize()

        # Hash the key to find the right bucket
        keyHash = hash(key)
        index = abs(keyHash) % self.capacity
        bucket = self.buckets[index]

        #check if key is already exists
        for entry in bucket:
            if entry.getKey() == key:
                return False #Key already exists, do not add
        
        new_entry = self.MyHashMapEntry(key, value)
        bucket.append(new_entry)
        self.size += 1
        return True
       
    """
    Replaces the value that maps to the given key if it is present.
    Input: key is the key whose mapped value is being replaced.
           newValue is the value to replace the existing value with.
    Return true if the key was in this MyHashMap and replaced successfully.
    Raise an exception if the key is None. """
    def replace(self, key, newValue):
       if key is None:
           raise Exception("Key cannot be None")
       index = self.get_bucket_index(key)
       bucket = self.buckets[index]
       for entry in bucket:
           if entry.getKey() == key:
               entry.setValue(newValue)
               return True
           return False  #Key not found
       
    """
    Remove the entry corresponding to the given key.
    Return true if an entry for the given key was removed.
    Raise an exception if the key is None. """
    def remove(self, key):
       if key is None:
           raise Exception("Key cannot be None")
       index = self.get_bucket_index(key)
       bucket = self.buckets[index]
       for entry in bucket:
           if entry.getKey() == key:
               bucket.remove(entry)
               self.size -= 1
               return True
           return False  #Key not found

    """
    Adds the key, value pair to the MyHashMap if it is not present.
    Otherwise, replace the existing value for that key with the given value.
    Raise an exception if the key is None. """
    def set(self, key, value):
        if key is None:
            raise Exception("Key cannot be None")
        # If key exists, update it. If not, add it
        if self.replace(key, value):
            return
        self.put(key, value)

    """
    Return the value of the specified key. If the key is not in the
    MyHashMap, return None.
    Raise an exception if the key is None. """
    def get(self, key):
        if key is None:
           raise Exception("Key cannot be None")
        index = self.get_bucket_index(key)
        bucket = self.buckets[index]
        for entry in bucket:
            if entry.getKey() == key:
                return entry.getValue()
            return None

    """
    Return the number of key, value pairs in this MyHashMap. """
    def get_size(self):
        return self.size

    """
    Return true if the MyHashMap contains no elements, and 
    false otherwise. """
    def isEmpty(self):
        return self.size == 0

    """
    Return true if the specified key is in this MyHashMap. 
    Raise an exception if the key is None. """
    def containsKey(self, key):
        if key is None:
            raise Exception("Key cannot be None")
        index = self.get_bucket_index(key)
        bucket = self.buckets[index]
        for entry in bucket:
            if entry.getKey() == key:
                return True
            return False
    """
    Return a list containing the keys of this MyHashMap. 
    If it is empty, return an empty list. """
    def keys(self):
       all_keys = []
       for bucket in self.buckets:
           for entry in bucket:
               all_keys.append(entry.getKey())
               return all_keys

    class MyHashMapEntry:
        def __init__(self, key, value):
            self.key = key 
            self.value = value 

        def getKey(self):
            return self.key 
        
        def getValue(self):
            return self.value 
        
        def setValue(self, new_value):
            self.value = new_value 

if __name__ == "__main__":
    my_map = MyHashMap()

    print(my_map.put("apple", 1))  #True
    print(my_map.put("banana", 2))  #True
    print(my_map.put("apple", 99)) #False
    print(my_map.get("apple"))  #1
    print(my_map.get_size())    #2
    print(my_map.isEmpty())