class MyStack:

    def __init__(self):
        self.q = deque()        

    def push(self, x: int) -> None:
        self.q = deque((x,self.q))    

    def pop(self) -> int:
        value, self.q = self.q
        return value
        

    def top(self) -> int:
        return self.q[0]
        
    def empty(self) -> bool:
        return not self.q

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()