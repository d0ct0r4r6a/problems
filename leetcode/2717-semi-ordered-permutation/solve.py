class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        nIndex = nums.index(len(nums))
        oneIndex = nums.index(1)
        return (len(nums) - 1 - nIndex) + oneIndex + (-1 if oneIndex > nIndex else 0)