import math

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        mapPos = {}
        for i, pos in enumerate(position):
            mapPos[pos] = speed[i]
        mapPos = dict(sorted(mapPos.items(), key=lambda item: item[0]))
        for pos in mapPos:
            time = (target - pos) / mapPos[pos]
            #print(pos, mapPos[pos], time)
            while len(stack) != 0 and stack[-1] <= time:
                stack.pop()
            stack.append(time)
            #print(stack)             
        return len(stack)
        