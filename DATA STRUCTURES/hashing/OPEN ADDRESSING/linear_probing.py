class Linear:
    def __init__(self,bucket):
        self.bucket=bucket
        self.hashTable=[None]*bucket
    def insert(self,key):
        idx=key%self.bucket
        while idx<self.bucket:
            if self.hashTable[idx]==None:
                self.hashTable[idx]=key
                break
            idx+=1
            if idx>=self.bucket:
                idx=0
                if self.hashTable[idx]==None:
                    self.hashTable[idx]=key
                    break
        # print(self.hashTable)
    def remove(self, key):
        idx=self.hashTable.index(key)
        self.hashTable[idx]="deleted"
        print(self.hashTable)
    def search(self,key):
        if key in self.hashTable:
            return print("yes")
        else:
            return print("no")
h=Linear(7)
h.insert(56)
h.insert(49)
h.insert(55)
h.insert(48)
h.remove(48)
h.search(55)

