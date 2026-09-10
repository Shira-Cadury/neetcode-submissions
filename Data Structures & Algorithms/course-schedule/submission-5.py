class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if numCourses == 0:
            return True

        adj = [[] for _ in range(numCourses)]

        for a, b in prerequisites:
            adj[b].append(a) 
        color = numCourses * [0]    

        def dfs(course):
            if color[course] == 1:
                return False

            if color[course] == 2:
                return True

            color[course] = 1
            for n in adj[course]:
                if not dfs(n):
                    return False
            color[course] = 2
            return True   

        for n in range(numCourses):
            if color[n] == 0:
                if not dfs(n):
                    return False
        return True                 

        