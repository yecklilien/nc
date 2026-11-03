class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R = len(board)
        C = len(board[0])

        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        def dfs(r, c, i):
            if i == len(word)-1:    
                return True
            
            res = False
            for nr,nc in dirs:
                if r + nr >=0 and r+nr < R and c+nc >= 0 and c+nc < C:
                    if board[r+nr][c+nc] == word[i+1]:
                        board[r+nr][c+nc] = '#'
                        res = res or dfs(r+nr,c+nc,i+1)
                        board[r+nr][c+nc] = word[i+1]
            
            return res
        
        for r in range(R):
            for c in range(C):
                if board[r][c] == word[0]:
                    board[r][c] = '#'
                    if dfs(r,c,0):
                        return True
                    board[r][c] = word[0]
                
        return False