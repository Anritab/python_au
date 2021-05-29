## K Closest Points to Origin
https://leetcode.com/problems/k-closest-points-to-origin/
```python
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        parents = Counter()
        graph = defaultdict(list)
        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
            parents[course] += 1
        courses = []
        queue = []
        for n in range(numCourses):
            if parents[n] == 0:
                queue.append(n)
        while queue:
            node = queue.pop(0)
            courses.append(node)
            for child in graph[node]:
                parents[child] -= 1
                if parents[child] == 0:
                    queue.append(child)
        if len(courses) == numCourses:
            return courses
```
