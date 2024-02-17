# ------------------------------------------------------------
# ST1507 DSAA
# CA2 Assignment
#
# Write a Python program to implement hashtable
# 
# ------------------------------------------------------------
#
# Author: Goh Rui Zhuo, Bharathan Bhaskaran
# StudentID: 2222329
# Class: DAAA/FT/2B/05
# Date: 4-Jan-2024
# Filename: hashTable.py
#
# ------------------------------------------------------------

# Creation of hash table here for data storage
class hashTable:

    '''
    Create a init with different attributes here
    '''
    def __init__(self, size=5):
        self.size = size
        self.keys = [None] * self.size
        self.buckets = [None] * self.size
        self.count = 0


    '''
    Create a hash function that see if it is a int or a str and if it's a string it covnerts using the order ascii charater to store
    '''
    def hashFunc(self, key):

        # If it is an integer just return the key % self.size here
        if isinstance(key, int):
            return key % self.size
        
        # IF it is a string, then get the ascii character then % self.size for efficient storage
        elif isinstance(key, str):
            hashVal = 0
            for char in key:
                hashVal = (hashVal * 31 + ord(char)) % self.size
            return hashVal
    
    '''
    The rehashfunction incase of collison here to move to the next index here
    '''
    def rehashFunc(self, old_hash):
        return (int(old_hash) + 1) % self.size
    
    '''
    The resize function to resize incase the current storage is not enough here
    '''
    def resize(self):

        # Getting the old size here
        oldSize = self.size

        # Setting the new size to be two times of it
        self.size *= 2

        # Getting the old keys and buckets 
        oldKeys = self.keys
        oldBuckets = self.buckets

        # Setting the current new keys and buckets to the new size here
        self.keys = [None] * self.size
        self.buckets = [None] * self.size

        # Insert back the old values into both the buckets and keys
        for i in range(oldSize):
            if oldKeys[i] is not None:
                self.__insert(oldKeys[i], oldBuckets[i])
    
    '''
    The items function to get the items from the hash table here
    '''
    def items(self):
        for i in range(self.size):
            if self.keys[i] is not None:
                yield (self.keys[i], self.buckets[i])
    
    '''
    The insert function is used to insert the key and value
    '''
    def __insert(self, key, value):

        # Getting the inex first
        index = self.hashFunc(key)

        # Check if the keys is not none then insert here
        while self.keys[index] is not None:
            index = self.rehashFunc(index)
        
        # Setting the new key and value here
        self.keys[index] = key
        self.buckets[index] = value
    
    '''
    Set item overloading set item function here
    '''
    def __setitem__(self, key, value):

        # Check if the need to resize the hashtable
        if self.count / self.size >= 0.8:
            self.resize()
        
        # get the index using the key
        index = self.hashFunc(key)

        # setting the start index here
        startIdx = index

        # While loop here 
        while True:

            # If the index at both the buckets and keys is none or that they keys is equal to the key 
            if self.buckets[index] is None or self.keys[index] == key:

                # If the buckets is none
                if self.buckets[index] is None:

                    # Increment the count by 1 here
                    self.count += 1
                
                # Setting the keys and buckets here
                self.keys[index] = key
                self.buckets[index] = value

                # Break the loop once all done
                break
                
            # Rehash the function to get the new index
            else:
                index  = self.rehashFunc(index)
    
    '''
    Get item overloading set item function here
    '''
    def __getitem__(self, key):

        # Getting the index base on the key
        index = self.hashFunc(key)

        # Set the start index here
        startIdx = index

        # While loop here
        while True:

            # If the keys at that indexis equal to what we are tyring to find then return the value
            if self.keys[index] == key:
                return self.buckets[index]  
            
            # Else return none here
            elif self.keys[index] is None:
                return None  

            # If unable to find and keys not none then rehash here
            index = self.rehashFunc(index)

            # If the rehash equal to the start index , it means it return to the original postion and therefore return none here
            if index == startIdx:
                return None
    
    '''
    Contains item overloading set item function here
    '''
    def __contains__(self, key):
        # Getting the index base on the key
        index = self.hashFunc(key)

        # Set the start index here
        startIdx = index

        # While loop here
        while True:

            # If the keys at that indexis equal to what we are tyring to find then return the true
            if self.keys[index] == key:
                return True

             # Else return false here
            elif self.keys[index] is None:
                return False  

            # If unable to find and keys not none then rehash here
            index = self.rehashFunc(index)

            # If the rehash equal to the start index , it means it return to the original postion and therefore return none here
            if index == startIdx:
                return None

    '''
    Delete item overloading set item function here
    '''
    def __delitem__(self, key):

        # if the key exist here
        if key in self:

            # Getting the index here and set the start index
            index = self.hashFunc(key)
            startIdx = index

            # While loop here
            while True:

                # If the gotten key is equal to the target, proceed to set to none
                if self.keys[index] == key:
                    self.keys[index] = None
                    self.buckets[index] = None

                    # Reduce the count by 1 and return
                    self.count -= 1
                    return  
                else:
                    # If unable to find and keys not none then rehash here
                    index = self.rehashFunc(index)

                    # If the rehash equal to the start index , it means it return to the original postion and therefore return none here
                    if index == startIdx:
                        return None
            
            # Return the key not found here
            return (f"Key: {key} not found")
        else:
            return (f"Key: {key} not found")

    def get(self, key, default=None):
        # Getting the index base on the key
        index = self.hashFunc(key)

        # Set the start index here
        startIdx = index

        # While loop here
        while True:

            # If the keys at that indexis equal to what we are tyring to find then return the value
            if self.keys[index] == key:
                return self.buckets[index]  
            
            # Else return none here
            elif self.keys[index] is None:
                return default  

            # If unable to find and keys not none then rehash here
            index = self.rehashFunc(index)

            # If the rehash equal to the start index , it means it return to the original postion and therefore return none here
            if index == startIdx:
                return default
    
    ''' A print hash function to see what is inside here'''
    def printHash(self):

        # Looping through the hash table and printing the key value pair
        for i in range(self.size):
            if self.keys[i] is not None:
                print(f"Key: {self.keys[i]}, Value: {self.buckets[i]}")
