class Solution:
    def rob(self, nums: List[int]) -> int:
        money = [0, nums[0]]
        for houseNumber in range(2, len(nums) + 1):
            previousHouseMoney = money[houseNumber - 1]
            if (money[houseNumber - 2] + nums[houseNumber - 1] > previousHouseMoney):
                money.append(money[houseNumber - 2] + nums[houseNumber - 1])
            else:
                money.append(previousHouseMoney)
        return money[-1]
