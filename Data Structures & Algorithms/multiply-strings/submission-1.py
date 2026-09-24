class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        char_to_digit = {
            '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
            '5': 5, '6': 6, '7': 7, '8': 8, '9': 9
        }

        res = [0] * (len(num1) + len(num2))

        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                mul = char_to_digit[num1[i]] * char_to_digit[num2[j]]
                total = mul + res[i + j + 1]
                res[i + j + 1] = total % 10
                res[i + j] += total // 10

        result_str = "".join(map(str, res)).lstrip('0')
        return result_str if result_str else "0"        
        