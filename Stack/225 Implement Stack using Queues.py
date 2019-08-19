class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = []
        self.q2 = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q1.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if self.q1:
            while len(self.q1) > 1:
                self.q2.append(self.q1.pop(0))
            output = self.q1.pop()
            while len(self.q2):
                self.q1.append(self.q2.pop(0))
            return output
        else:
            return False

    def top(self) -> int:
        """
        Get the top element.
        """
        if self.q1:
            while len(self.q1) > 1:
                self.q2.append(self.q1.pop(0))
            output = self.q1.pop()
            self.q2.append(output)
            while len(self.q2):
                self.q1.append(self.q2.pop(0))
            return output
        else:
            return False

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.q1 == []

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()