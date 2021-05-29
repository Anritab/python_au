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
## Number of Islands
https://leetcode.com/problems/number-of-islands/
```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans, m, n = 0, len(grid), len(grid[0])
        def dfs(row, col):
            if  0 <= row < m and 0 <= col < n and grid[row][col] == "1":
                grid[row][col] = "0"
                for x, y in [(1,0),(-1,0),(0,1),(0,-1)]:
                    dfs(row + x , col + y)
                
        for row in range(m):
            for col in range(n):
                if grid[row][col] == '1':
                    dfs(row, col)
                    ans += 1
        return ans
```
## Is Graph Bipartite?
https://leetcode.com/problems/is-graph-bipartite/
```python
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [0]*len(graph)
        for i in range(len(graph)):
            if color[i] == 0:
                q = deque()
                q.append((i, 1))
                while(q):
                    node, ncolor = q.popleft() 
                    if color[node] == 0: 
                        color[node] = ncolor 
                        for nx in graph[node]:
                            q.append((nx, -ncolor))
                    if color[node] != ncolor:
                        return False
        return True
```
## Cheapest Flights Within K Stops
https://leetcode.com/problems/cheapest-flights-within-k-stops/
```python
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        G = defaultdict(set)
        for f, t, p in flights: 
            G[f].add((t, p))
        P = defaultdict(lambda: inf)
        res = inf
        q = [(src, 0, 0)]
        for loc, price, stops in q: 
            if stops > k + 1: 
                break
            if loc == dst: 
                res = min(res, price)
            for to, p in G[loc]: 
                if P[to] > price + p: 
                    P[to] = price + p
                    q.append((to, price + p, stops + 1))   
        return res if res < inf else -1
```
## Shortest Path in Binary Matrix
https://leetcode.com/problems/shortest-path-in-binary-matrix/
```python
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n=len(grid)
        if grid[0][0] or grid[-1][-1]:
            return -1
        queue=[(0,0,1)]
        dir=[(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        for i,j,d in queue:
            if i==n-1 and j==n-1:
                return d
            for x,y in dir:
                row=i+x
                col=j+y
                if 0<=row<n and 0<=col<n and not grid[row][col]:
                    queue.append((row,col,d+1))
                    grid[row][col]=1
        return -1
```
