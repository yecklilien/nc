class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = -1
        l = 0
        r = len(heights)-1
        while l < r:
            mostWater = min(heights[l], heights[r]) * (r-l)
            if mostWater > result:
                result = mostWater
            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            else:
                l+=1
                r-=1
        return result

        