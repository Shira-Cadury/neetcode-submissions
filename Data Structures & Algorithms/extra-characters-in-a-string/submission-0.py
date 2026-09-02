class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        root = TrieNode()
        for word in dictionary:
            curr = root
            for c in word:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.is_end_of_word = True

        memo = {}

        def dfs(i: int) -> int:
            if i == len(s):
                return 0
            if i in memo:
                return memo[i]

            res = 1 + dfs(i + 1)

            curr = root
            for j in range(i, len(s)):
                c = s[j]
                if c not in curr.children:
                    break
                curr = curr.children[c]
                if curr.is_end_of_word:
                    res = min(res, dfs(j + 1))

            memo[i] = res
            return res

        return dfs(0)