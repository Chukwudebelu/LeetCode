class MyQueue(object):
    def __init__(self):
        """Initialize the queue using a list object"""
        self.Q = []   

    def push(self, x: int) -> None:
        """Push element x to the back of the queue"""
        self.Q += [x]

    def pop(self) -> int:
        """Remove the element from the front of the queue
           and return it"""
        elementOne = self.Q[0]
        del self.Q[0]
        return elementOne

    def peek(self) -> int:
        """Returns the element at the front of the queue"""
        return self.Q[-len(self.Q)]        

    def empty(self) -> bool:
        """Returns 'true' if the queue is empty, 'false' otherwise"""
        return True if (len(self.Q) == 0) else False    


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
