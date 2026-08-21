class MyHashSet:

    def __init__(self):
       self.size = 1000
       self.table = [[] for _ in range(self.size)] 

    def add(self, key: int) -> None:
        index = key % self.size
        bucket = self.table[index]
        if key in bucket:
            return
        bucket.append(key)    

    def remove(self, key: int) -> None:
        index = key % self.size
        bucket = self.table[index]
        if key in bucket:
            bucket.remove(key)

    def contains(self, key: int) -> bool:
        index = key % self.size
        bucket = self.table[index]
        if key in bucket:
            return True
        return False    


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)