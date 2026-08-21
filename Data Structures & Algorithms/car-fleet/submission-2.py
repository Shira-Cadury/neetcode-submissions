class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        stuck = []
        for p,s in cars:
            time = (target - p) / s
            if not stuck or time > stuck[-1]:
                stuck.append(time)
        return len(stuck)        