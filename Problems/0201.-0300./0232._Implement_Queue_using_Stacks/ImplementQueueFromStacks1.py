class MyQueue(object):
    def __init__(self):
        """Initialize the queue using a list object"""
        self.stack = []   

    def push(self, x: int) -> None:
        """Push element x to the back of the queue"""
        self.stack += [x]

    def pop(self) -> int:
        """Remove the element from the front of the queue
           and return it"""
        elementOne = self.stack[0]
        del self.stack[0]
        return elementOne

    def peek(self) -> int:
        """Returns the element at the front of the queue"""
        return self.stack[-len(self.stack)]        

    def empty(self) -> bool:
        """Returns 'true' if the queue is empty, 'false' otherwise"""
        return True if (len(self.stack) == 0) else False    


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
