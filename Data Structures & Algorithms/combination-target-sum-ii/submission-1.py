class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def helper(start, curr, target):
            if target == 0:
                res.append(curr[:])
                return
            if target < 0:
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                
                curr.append(candidates[i])
                helper(i + 1, curr, target - candidates[i])
                curr.pop()

        helper(0, [], target)
        return res