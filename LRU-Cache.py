class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value

        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, cap: int):
        self.cap = cap
        self.cache = {}

        self.head = Node(0,0)
        self.tail = Node(0,0)

        self.head.next = self.tail
        self.tail.prev = self.head

    def  remove(self,node):
        nxt = node.next 
        prev = node.prev

        prev.next = nxt
        nxt.prev = prev

    def insertafterHead(self,node):

        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        
    def get(self, key: int) -> int:

        if key in self.cache:

            node = self.cache[key]
            self.remove(node)
            self.insertafterHead(node)
            return node.value

        return -1
        
    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.remove(node)
            self.insertafterHead(node)

        else:
            newNode = Node(key,value)
            self.insertafterHead(newNode)
            self.cache[key]=newNode

            if len(self.cache)>self.cap:
                lru = self.tail.prev
                self.remove(lru)
                del self.cache[lru.key]
                
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)