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
## Implement Stack using Queues
https://leetcode.com/problems/implement-stack-using-queues/
```python
class MyStack:
    def __init__(self):
        self.stack=[]
    def push(self, x):
        self.stack.append(x)
    def pop(self):
        return self.stack.pop(-1)
    def top(self):
        return self.stack[-1]
    def empty(self):
        return len(self.stack) == 0
```
## Design Twitter
https://leetcode.com/problems/design-twitter/
```python
class Twitter:
    def __init__(self):
        self.stack = list()
        self.fo = defaultdict(list)
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.stack.append([userId,tweetId])
    def getNewsFeed(self, userId: int) -> List[int]:
        temp = list()
        for i in range(len(self.stack)-1,-1,-1):
            if self.stack[i][0]==userId or self.stack[i][0] in self.fo[userId]:
                temp.append(self.stack[i][1])
                if len(temp)==10:
                    break
        return temp
    def follow(self, followerId: int, followeeId: int) -> None:
        self.fo[followerId].append(followeeId)
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.fo[followerId]:
            self.fo[followerId].remove(followeeId)
```
