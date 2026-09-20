class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        l = 0
        r = len(height) - 1
        max_left = -1
        max_right = -1
        while(l<r):
            if height[l] > max_left:
                max_left = height[l]
            if height[r] > max_right:
                max_right = height[r]

            if max_left < max_right:
                result += max_left - height[l]
                l+=1
            else:
                result += max_right - height[r]
                r-=1
        return result


# 0,1,0,2,1,0,1,3,2,1,2,1
# 0,1,1,2,2,2,2,3,3,3,3,3
# 3,3,3,3,3,3,3,3,2,2,2,1
# 0,0,1,0,1,2,1,0,1,1,0,0

# 0 2 0 3 1 0 1 3 2 1 
# 0 2 2 3 3 3 3 3 3 3 
# 3 3 3 3 3 3 3 3 2 1