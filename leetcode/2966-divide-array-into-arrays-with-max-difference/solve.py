class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        if len(nums) % 3 != 0:
            return []
        nums.sort()
        ans = []
        for i in range(round(len(nums) / 3)):
            index = i * 3
            if nums[index + 2] - nums[index] > k:
                return []
            ans.append(nums[index:index+3])
        return ans