# Function to display hashtable
def display_hash(hashTable):
    for i in range(len(hashTable)):
        print(i, end=" ")

        for j in hashTable[i]:
            print("-->", end=" ")
            print(j, end=" ")

        print()


# Creating Hashtable as
# a nested list.
HashTable = [[] for _ in range(10)]

def Hashing(keyvalue):
    return keyvalue % len(HashTable)


# Insert Function to add
# values to the hash table
def insert(Hashtable, keyvalue, value):
    hash_key = Hashing(keyvalue)
    Hashtable[hash_key].append(value)


# Driver Code
insert(HashTable, 10, 'Anne')
insert(HashTable, 25, 'Nicole')
insert(HashTable, 20, 'Mejia')
insert(HashTable, 9, 'Ines')
insert(HashTable, 21, 'Mejia')
insert(HashTable, 21, 'Kowlee')

display_hash(HashTable)
