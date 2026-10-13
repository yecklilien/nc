from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def flood(grid, ri, ci):
            x = [-1,1,0,0]
            y = [0,0,-1,1]
            q = deque()
            grid[ri][ci] = "0"
            q.append((ri,ci))
            while (len(q)>0):
                r,c = q.popleft()
                for i in range(4):
                    if r+y[i] >=0 and r+y[i] <len(grid) and c+x[i] >=0 and c+x[i] <len(grid[r]):
                        if grid[r+y[i]][c+x[i]] == "1":
                            grid[r+y[i]][c+x[i]] = "0"
                            q.append((r+y[i], c+x[i]))
    
        res = 0
        for r in range (len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == "1":
                    res += 1
                    flood(grid, r, c)
        return res        
        
        