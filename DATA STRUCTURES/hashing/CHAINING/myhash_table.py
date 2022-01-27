class MyHashTable():
    def __init__(self,bucket):
        self.bucket=bucket
        self.hashTable=[[] for  i  in range(bucket)]
        # print (hashTable)
    def insert(self,key):
        idx=key%self.bucket
        self.hashTable[idx].append(key)
        # print(self.hashTable)
    def remove(self,key):
        idx=key%self.bucket
        self.hashTable[idx].remove(key)
        # print(self.hashTable)
    def search(self,key):
        idx=key%self.bucket
        if key in self.hashTable[idx]:
                return print("yes")
        else:
            return print("no")


h = MyHashTable(7)
h.insert(56)
h.insert(70)
h.insert(55)
h.remove(70)
h.search(55)

