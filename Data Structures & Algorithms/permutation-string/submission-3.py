class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1 = len(s1)
        len_s2 = len(s2)
        if len_s1 > len_s2:
            return False
        count1 = [0] * 26
        count2 = [0] * 26
        left = 0
        for i in range(len_s1):
            count1[ord(s1[i]) - ord('a')] += 1
        for i in range(len_s1):
            count2[ord(s2[i]) - ord('a')] += 1
        if count1 == count2:
            return True
        for i in range(len_s1, len_s2):
            count2[ord(s2[left]) - ord('a')] -= 1
            left += 1
            count2[ord(s2[i]) - ord('a')] += 1
            if count1 == count2:
                return True
        return False        