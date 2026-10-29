class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [-1] * n
        def recurse(idx):
            if idx == n:
                return 1
            if idx > n:
                return 0
            if cache[idx] != - 1:
                return cache[idx]
        
            cache[idx] =  recurse(idx + 1) + recurse(idx + 2)
            return cache[idx]

        return recurse(0)
                