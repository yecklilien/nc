class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # tuple (day, temperature)
        stack = [(0, temperatures[0])]
        result = [0 for _ in range(len(temperatures))]

        for day in range(1,len(temperatures),1):
            while len(stack) > 0 and stack[-1][1] < temperatures[day]:
                result[stack[-1][0]] = day - stack[-1][0]
                stack.pop()
            stack.append((day, temperatures[day]))
        
        return result
            
