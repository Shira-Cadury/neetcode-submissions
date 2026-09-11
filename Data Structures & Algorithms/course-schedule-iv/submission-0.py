class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = [[] for _  in range(numCourses)]
        for a, b in prerequisites:
            adj[a].append(b)
        reachable = [set() for _ in range(numCourses)]    

        def dfs(curr, start):
            for n in adj[curr]:
                if n not in reachable[start]:
                    reachable[start].add(n)
                    dfs(n, start)
            return
        for i in range(numCourses):
            dfs(i, i)  
        ans = []
        for u, v in queries:
            ans.append(v in reachable[u])
        return ans              
        