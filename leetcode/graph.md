## Course Schedule II
https://leetcode.com/problems/course-schedule-ii/
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
## Course Schedule
https://leetcode.com/problems/course-schedule/
```python
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
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
            return True
        return False
```
