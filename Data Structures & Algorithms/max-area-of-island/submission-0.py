from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        LROWS = len(grid)
        LCOLS = len(grid[0])
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]

        def flood(grid, r, c):
            res = 1
            q = deque()
            grid[r][c] = 0
            q.append((r,c))
            while len(q) > 0:
                r,c = q.popleft()
                for x,y in (dirs):
                    nr = r+y
                    nc = c+x
                    if nr>= 0 and nr < LROWS and nc >= 0 and nc < LCOLS and grid[nr][nc] == 1:
                        res+=1
                        grid[nr][nc] = 0
                        q.append((nr,nc))
            return res                         

        res = 0
        for r in range(LROWS):
            for c in range(LCOLS):
                if grid[r][c] == 1:
                    res = max(res, flood(grid, r,c))
        return res
