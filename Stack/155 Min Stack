class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.items = []
        self.min = None

    def push(self, x: int) -> None:
        if self.items == [] or x < self.min:
            self.min = x
        self.items.append((x, self.min))

    def pop(self) -> None:
        if self.items:
            self.items.pop()
        if self.items:
            x, self.min = self.items[-1]
        else:
            self.min = None
        return

    def top(self) -> int:
        if self.items:
            data, x = self.items[-1]
            return data

    def getMin(self) -> int:
        if self.items:
            x, m = self.items[-1]
            return m

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
