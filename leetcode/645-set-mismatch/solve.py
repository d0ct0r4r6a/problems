class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        c = collections.Counter(nums)
        for i in range(1, len(nums) + 1):
            if c[i] == 0:
                missing = i
            if c[i] == 2:
                duplicate = i
        return [duplicate, missing]
