class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        minCost = cost[0:2]
        for i in range(2, len(cost)):
            minCost.append(min(minCost[i - 2], minCost[i - 1]) + cost[i])
        return min(minCost[-2:])
