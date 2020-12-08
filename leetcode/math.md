## Reverse Integer
https://leetcode.com/problems/reverse-integer/
```python
    def reverse(self, x: int) -> int:
        flag = 0
        if x < 0:
            flag = 1
            x = abs(x)
        x = str(x)  #почему
        y = ""
        for i in range(len(x) - 1, -1, -1):
            y += x[i]
        y = int(y)  #потому
        if flag == 1:
            y = - y
        if y > 2 ** 31 - 1 or y < - 2 ** 31:
            return 0
        return y
```
## Palindrome Number
https://leetcode.com/problems/palindrome-number/
```python
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        y = ""
        for i in range(len(x) - 1, -1, -1):
            y += x[i]
        if y == x:
            return True
        return False
```
## Fizz Buzz
https://leetcode.com/problems/fizz-buzz/
```python
    def fizzBuzz(self, n: int) -> List[str]:
        a = []
        for i in range(1, n + 1):
            if i % 15 == 0:
                a.append("FizzBuzz")
            elif i % 5 == 0:
                a.append("Buzz")
            elif i % 3 == 0:
                a.append("Fizz")
            else:
                a.append(str(i))
        return a
```
## Largest Perimeter Triangle
https://leetcode.com/problems/largest-perimeter-triangle/
```python
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort()
        for i in range(len(A) - 1, 1, -1):
            if A[i] < A[i-1] + A[i-2]:
                return A[i] + A[i-1] + A[i-2] 
        return 0
```
## Sqrt(x)
https://leetcode.com/problems/sqrtx/
```python
    def mySqrt(self, x: int) -> int:
        return int(x ** 0.5)
```
