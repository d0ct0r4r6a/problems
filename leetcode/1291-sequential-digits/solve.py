class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        digits = '123456789'
        ans = []
        for n in range(len(low), len(high) + 1):
            for i in range(10 - n):
                subdigits = int(digits[i:i+n])
                if subdigits >= low and subdigits <= high:
                    ans.append(subdigits)
        return ans