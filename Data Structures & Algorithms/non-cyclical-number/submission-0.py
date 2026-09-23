class Solution:
    def isHappy(self, n: int) -> bool:
        def getNext(number):
            total_sum = 0
            while number:
                digit = number % 10
                total_sum += digit * digit
                number = number // 10
            return total_sum

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = getNext(n)

        return n == 1
            