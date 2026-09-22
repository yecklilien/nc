class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        result = 0
        for i, height in enumerate(heights):
            prevPos = i
            while stack and stack[-1][1] >= heights[i]:
                prevHeight = stack.pop()
                prevPos = prevHeight[0]
                area =  (i - prevHeight[0]) * prevHeight[1]
                if area > result:
                    result = area
            stack.append([prevPos,height])
        
        while stack:
            prevHeight = stack.pop()
            area = (len(heights) - prevHeight[0]) * prevHeight[1] 
            if area > result:
                result = area
        
        return result