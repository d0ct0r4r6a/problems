def get_bin(num):
    return '{0:b}'.format(num)

def check_uniq(arr):
    joined = ''.join(arr)
    counter = collections.Counter([*joined])
    for freq in counter.values():
        if freq > 1:
            return False
    return True

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        N = len(arr)
        numForBits = 2 ** N - 1
        ans = 0
        ansLen = 0
        while (numForBits > 0):
            binStr = get_bin(numForBits).rjust(N, '0')
            selectedArr = [elem for i, elem in enumerate(arr) if binStr[i] == '1']
            if (check_uniq(selectedArr)):
                length = len(''.join(selectedArr))
                if (length > ans):
                    ans = length
            numForBits -= 1
        return ans

