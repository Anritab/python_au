## Max Consecutive Ones
https://leetcode.com/problems/max-consecutive-ones/
```python
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        a = []
        count = 0
        for i in nums:
            if i == 1:
                count += 1
            else:
                a.append(count)
                count = 0
        a.append(count)
        return max(a)
```
## Reshape the Matrix
https://leetcode.com/problems/reshape-the-matrix/
```python
class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(nums) * len(nums[0]) != r * c:
            return nums
        
        a = []  
        b = []
        for i in range(len(nums)):
            for j in range(len(nums[0])):
                if len(b) == c:
                    a.append(b)
                    b = []
                b.append(nums[i][j])  
        a.append(b)
        return a
```
## Image Smoother
https://leetcode.com/problems/image-smoother/
```python
class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        a = []
        b = len(M)
        c = len(M[0])
        for i, p in enumerate(M):
            a2 = []
            for j, q in enumerate(M[i]):
                k = M[i][j]
                n = 1
                
                if i > 0:
                    m1 = M[i-1][max(0, j-1):min(j+2, c)]
                    n += len(m1)
                    k += sum(m1)
                if i < b - 1:
                    m0 = M[i+1][max(0, j-1):min(j+2, c)]
                    n += len(m0)
                    k += sum(m0)
                if j > 0:
                    n += 1
                    k += M[i][j-1]
                if j < c - 1:
                    n += 1
                    k += M[i][j+1]
                a2.append(math.floor(k / n))
            a.append(a2)
        return a
```
## Flipping an Image
https://leetcode.com/problems/flipping-an-image/
```python
class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for i in A:
            i.reverse()
            for j in range (len(i)):
                if i[j] == 0:
                    i[j] = 1
                else:
                    i[j] = 0
        return A
```
## Transpose Matrix
https://leetcode.com/problems/transpose-matrix/
```python
class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        a = len(A)
        b = len(A[0])
        N = [[0] * a for i in range(b)]
        for i in range(a):
            for j in range(b):
                N[j][i] = A[i][j]   
        return N
```
## Move Zeroes
https://leetcode.com/problems/move-zeroes/submissions/
```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        for i in nums:
            if i == 0:
                nums.remove(i)
                nums.append(i)
        return nums
```
## Squares of a Sorted Array
https://leetcode.com/problems/squares-of-a-sorted-array/
```python
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        a = []
        for i in nums:
            a += i**2,
        return sorted(a)
```
