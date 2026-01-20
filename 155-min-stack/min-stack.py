class MinStack:

    def __init__(self):
        # LIFO 
        # push to front, remove from front
        # push to back, remove from back <- better because o(1) amortized
        # no need to resize when pop from back but occasionally need to resize for insert to 
        self.stack = []
        self.mins = [] # min and stack 1 to 1 correspond to each other.

        

    def push(self, val: int) -> None:
        if len(self.mins) == 0:
            self.mins.append(val)
        else:
            self.mins.append(min(val, self.mins[-1]))
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.mins.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.mins[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()