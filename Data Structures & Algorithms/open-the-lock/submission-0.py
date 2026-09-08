class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if target == "0000":
            return 0

        visited = set(deadends)
        if "0000" in visited:
            return -1

        q = deque([("0000", 0)])
        visited.add("0000")

        while q:
            code, steps = q.popleft()

            for i in range(4):
                digit = int(code[i])
                
                up = str((digit + 1) % 10)
                down = str((digit - 1 + 10) % 10)
                
                next_up = code[:i] + up + code[i+1:]
                next_down = code[:i] + down + code[i+1:]

                for next_code in (next_up, next_down):
                    if next_code == target:
                        return steps + 1
                    
                    if next_code not in visited:
                        visited.add(next_code)
                        q.append((next_code, steps + 1))

        return -1