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
