class MyStack:

    def __init__(self):
        self.inarray = []
        self.outarray = []

    def push(self, x: int) -> None:
        self.inarray.append(x)
    def pop(self) -> int:
        while self.inarray:
            self.outarray.append(self.inarray.pop(0))
        while self.outarray:
            x = self.outarray.pop(0)
            if self.outarray == []:
                return x
            else:
                self.inarray.append(x)
    def top(self) -> int:
        while self.inarray:
            self.outarray.append(self.inarray.pop(0))
        while self.outarray:
            x = self.outarray.pop(0)
            self.inarray.append(x)
            if self.outarray == []:
                return x
                
    def empty(self) -> bool:
        return self.outarray==[] and self.inarray==[]


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()