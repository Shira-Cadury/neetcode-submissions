class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            adj[b].append(a)

        color = numCourses * [0]
        result = []

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
            result.append(course)
            return True

        for n in range(numCourses):
            if color[n] == 0:
                if not dfs(n):
                    return []
        return result[::-1]               
        