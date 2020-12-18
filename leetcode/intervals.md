## Non-overlapping Intervals
https://leetcode.com/problems/non-overlapping-intervals/
```python
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort()
        a = intervals[0][0]
        maxs = 0
        for i in intervals:
            if a > i[0]:
                a = min(a, i[1])
            else:
                maxs += 1
                a = i[1]        
        return len(intervals) - maxs
```
## Merge Intervals
https://leetcode.com/problems/merge-intervals/
```python
class Solution:
    def merge(self, intervals):
        intervals.sort()
        a = []
        x1 = intervals[0][0]
        x2 = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] > x2
                a.append([x1, x2])
                x1 = intervals[i][0]
                x2 = intervals[i][1]
            else:
                if intervals[i][1] > x2:
                    x2 = intervals[i][1]
        a.append([x1, x2])
        return a
```
## Insert Interval
https://leetcode.com/problems/insert-interval/
```python
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        if len(intervals) == 1:
            return intervals
        intervals.sort()
        a = [intervals[0]]
        for i in intervals[1:]:
            if i[0] <= a[-1][1]:
                a[-1][1] = max(a[-1][1], i[1])
            else:
                a.append(i)
        return a
```
