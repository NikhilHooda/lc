class RandomizedSet:

    def __init__(self):
        self.hashMap = {}
        self.numList = []

    def insert(self, val: int) -> bool:
        if val not in self.hashMap:
            idx = len(self.numList)
            self.numList.append(val)
            self.hashMap[val] = idx
            return True
        else:
            return False
    
    def remove(self, val: int) -> bool:
        if val in self.hashMap:
            idx = self.hashMap[val]
            value = self.numList[-1]
            self.numList[idx] = value
            self.hashMap[value] = idx
            self.numList.pop()
            del self.hashMap[val]
            return True
        else:
            return False
        
    def getRandom(self) -> int:
        return random.choice(self.numList)
         
#.   0,1,2
# set = {4:0}
# list = [4]
# random.choice(5) -> return bewteen 0 and 5

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()