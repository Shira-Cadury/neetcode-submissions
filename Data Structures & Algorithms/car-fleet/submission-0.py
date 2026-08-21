class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars = sorted(zip(position, speed), reverse=True)
        for p, s in cars:
            temp = (target - p) / s
            if not stack or temp > stack[-1]:
                stack.append(temp)
        return len(stack)           