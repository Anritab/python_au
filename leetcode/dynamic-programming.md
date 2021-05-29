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
## House Robber
https://leetcode.com/problems/house-robber/
```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        maxAmt = [None for i in range(len(nums) + 1)]
        N = len(nums)
        maxAmt[N] = 0
        maxAmt[N - 1] = nums[N - 1]
        for i in range(N - 2, -1, -1):
            maxAmt[i] = max(maxAmt[i + 1], maxAmt[i + 2] + nums[i])
        return maxAmt[0]
