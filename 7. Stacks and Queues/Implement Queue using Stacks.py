class MyQueue:

    def __init__(self):
        self.inarray = []
        self.outarray = []

    def push(self, x: int) -> None:
        while self.inarray != []:
            self.outarray.append(self.inarray.pop())
        self.outarray.append(x)

    def pop(self) -> int:
        while self.outarray != []:
            self.inarray.append(self.outarray.pop())
        return self.inarray.pop()
        
    def peek(self) -> int:
        while self.outarray != []:
            self.inarray.append(self.outarray.pop())
        return self.inarray[-1]
        

    def empty(self) -> bool:
        while self.inarray != []:
            self.outarray.append(self.inarray.pop())
        return self.outarray == []


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()