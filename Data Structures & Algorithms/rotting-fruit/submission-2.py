from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh_count = 0
        
        R = len(grid)
        C = len(grid[0])

        q = deque()

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    fresh_count += 1
                elif grid[r][c] == 2:
                    q.append((r,c))

        dirs = [(-1,0),(1,0),(0,-1),(0,1)]

        minutes = 0
        
        while fresh_count > 0 and len(q) > 0:
            for _ in range(len(q)):
                r,c = q.popleft()
                for nr,nc in dirs:
                    nextR = r+nr
                    nextC = c+nc
                    if nextR >=0 and nextR < R and nextC >= 0 and nextC < C and grid[nextR][nextC] == 1:
                        grid[nextR][nextC] = 2
                        fresh_count -= 1
                        q.append((nextR,nextC))
            minutes += 1

        if fresh_count == 0:
            return minutes
        else:
            return -1
            