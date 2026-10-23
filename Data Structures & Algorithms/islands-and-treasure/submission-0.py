from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        R, C = len(grid), len(grid[0])
        direction = [(1,0),(-1,0),(0,1),(0,-1)] #r,c
        q = deque()
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    q.append((r,c))
        
        distance = 1
        while len(q) > 0:
            for _ in range(len(q)):
                r,c = q.popleft()
                for dr, dc in direction:
                    nr = r + dr
                    nc = c + dc
                    if nr >= 0 and nr < R and nc >= 0 and nc < C and grid[nr][nc] != -1 and distance < grid[nr][nc]:
                        grid[nr][nc] = distance
                        q.append((nr,nc))
            distance += 1