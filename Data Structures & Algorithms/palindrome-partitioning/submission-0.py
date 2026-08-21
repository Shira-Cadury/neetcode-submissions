class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        def helper(curr, index):
            if index == len(s):
                res.append(curr[:])
                return
            for i in range(index, len(s)):
                temp=s[index : i+1]
                if temp == temp[:: -1]:
                    curr.append(temp)
                    helper(curr, i+1)
                    curr.pop()
        helper([], 0)
        return res            