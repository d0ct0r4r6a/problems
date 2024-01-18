cache = {}

def countSteps(n: int) -> int:
    if (n in cache):
        return cache[n]
    if (n <= 1):
        cache[n] = 1
        return cache[n]
    cache[n] = countSteps(n - 1) + countSteps(n - 2)
    return cache[n]

class Solution:
    def climbStairs(self, n: int) -> int:
        return countSteps(n)
