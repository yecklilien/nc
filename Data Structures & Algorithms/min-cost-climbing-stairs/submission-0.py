class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        memo = [-1] * (len(cost) + 1) 
        def recurse(i):
            if i<=1:
                return 0
            if memo[i] != -1:
                return memo[i]

            memo[i] = min(cost[i-1] + recurse(i-1), cost[i-2] + recurse(i-2))
            return memo[i]
        
        return recurse(len(cost))