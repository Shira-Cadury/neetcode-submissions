class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for w in word:
                count[ord(w) - ord('a')] += 1
            dic[tuple(count)].append(word)  
        return list(dic.values())