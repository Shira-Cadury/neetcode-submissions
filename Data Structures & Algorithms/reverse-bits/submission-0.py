class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = n & 1
            res |= (bit << (31 - i))
            n >>= 1
        return res
        