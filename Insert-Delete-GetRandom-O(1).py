class RandomizedSet:

    def __init__(self):

        self.st = []
        

    def insert(self, val: int) -> bool:

        if val not in self.st:
            self.st.append(val)
            return True
        else:
            return False
        

    def remove(self, val: int) -> bool:

        if val in self.st:
            self.st.remove(val)
            return True
        else:
            return False
        

    def getRandom(self) -> int:

        return random.choice(self.st)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()