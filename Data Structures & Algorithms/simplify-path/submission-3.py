class Solution:
    def simplifyPath(self, path: str) -> str:
        parts = path.split('/')
        stack = []
        for p in parts:
            if p == '' or p == '.':
                continue
            if p == '..':
                if stack:
                    stack.pop()
                continue
            stack.append(p)
        return "/" + "/".join(stack)                