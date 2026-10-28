from collections import deque
class Solution:
    def solve(self, grid: List[List[str]]) -> None:
        R = len(grid)
        C = len(grid[0])

        visited = [[False for _ in range(C)] for _ in range(R)]

        q = deque()
        def visitQueue(r,c,q,visited):
            if r < 0 or r >= R:
                return
            if c < 0 or c >= C:
                return
            if grid[r][c] != 'O' or visited[r][c]:
                return
            q.append((r,c))
            visited[r][c] = True
        
        for i in range(R):
            visitQueue(i,0,q,visited)
            visitQueue(i,C-1,q,visited)
        
        for i in range(C):
            visitQueue(0,i,q,visited)
            visitQueue(R-1,i,q,visited)
        
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        while len(q) > 0:
            r,c = q.popleft()
            for nr, nc in dirs:
                visitQueue(r+nr, c+nc, q, visited)
        
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 'O' and not visited[r][c]:
                    grid[r][c] = 'X'
            
