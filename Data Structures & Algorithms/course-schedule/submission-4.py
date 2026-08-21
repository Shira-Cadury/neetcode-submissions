class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses
        
        for course, pre in prerequisites:
            adj[pre].append(course)
            in_degree[course] += 1
            
        q = deque([i for i in range(numCourses) if in_degree[i] == 0])
        
        count = 0
        while q:
            curr = q.popleft()
            count += 1 
            
            for neighbor in adj[curr]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    q.append(neighbor)
        
        return count == numCourses
                          
