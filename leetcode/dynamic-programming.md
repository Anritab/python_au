## House Robber II
https://leetcode.com/problems/house-robber-ii/
```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        def robOneUtil(i,n,d):
            if i in d: return d[i]
            if i>=n:
                return 0
            d[i] = max(nums[i]+robOneUtil(i+2,n,d),robOneUtil(i+1,n,d))
            return d[i]
        def robTwoUtil(n):
            d1 = {}
            d2 = {}
            return max(robOneUtil(0,n-1,d1),robOneUtil(1,n,d2))
        return robTwoUtil(n)
```
