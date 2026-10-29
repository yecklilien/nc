class Solution:
    def climbStairs(self, n: int) -> int:
        res = [0] * (n+1)
        for i in range(1, n+1):
            if i<=2:
                res[i] = i
            else:
                res[i] = res[i-1] + res[i-2]
        
        return res[i]