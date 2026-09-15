class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        adj = defaultdict(list)
        for acc in accounts:
            firstEmail = acc[1]
            adj[firstEmail]
            for email in acc[2:]:
                adj[firstEmail].append(email)
                adj[email].append(firstEmail)

        def dfs(email, component):
            visited.add(email)
            component.append(email)
    
            for neighbor in adj[email]:
                if neighbor not in visited:
                    dfs(neighbor, component)

        res = []
        visited = set()

        for acc in accounts:
            firstEmail = acc[1]
            if firstEmail not in visited:
                component = []
                dfs(firstEmail, component)
                component.sort()
                name = acc[0] 
                res.append([name] + component)

        return res                    