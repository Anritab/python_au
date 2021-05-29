## Min Stack
https://leetcode.com/problems/min-stack/
```python
class MinStack:
    def __init__(self):
        self.stack = []
        self.stack_min = [float('inf')]
    def push(self, val: int) -> None:
        self.stack.append(val)
        if val<self.stack_min[-1]:
            self.stack_min.append(val)
        else:  
            self.stack_min.append(self.stack_min[-1])
    def pop(self) -> None:
        self.stack.pop()
        self.stack_min.pop()
    def top(self) -> int:
        return self.stack[-1]
    def getMin(self) -> int:
        return self.stack_min[-1]
```
## Implement Queue using Stacks
https://leetcode.com/problems/implement-queue-using-stacks/
```python
class Stack:
    def __init__(self):
        self.lst = []
    def push(self, x):
        self.lst.append(x)
    def pop(self):
        if len(self.lst) > 0:
            return self.lst.pop()
    def peek(self):
        if len(self.lst) > 0:
            return self.lst[-1]
    def empty(self):
        return len(self.lst) == 0
class MyQueue:
    def __init__(self):
        self.P = Stack()
        self.Q = Stack()
    def _QtoP(self):        
        if self.P.empty():
            while not self.Q.empty():
                self.P.push(self.Q.pop())
    def push(self, x: int) -> None:
        self.Q.push(x)        
    def pop(self) -> int:
        self._QtoP()                
        return self.P.pop()
    def peek(self) -> int:
        self._QtoP()
        return self.P.peek()
    def empty(self) -> bool:
        return self.P.empty() and self.Q.empty()        
```
