class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = [set() for _ in range(9)]
        column_set = [set() for _ in range(9)]
        box_set = [set() for _ in range(9)]

        for r in range (len(board)):
            for c in range (len(board[r])):
                val = board[r][c]
                if val != '.':
                    if val in row_set[r]:
                        return False
                    else:
                        row_set[r].add(val)

                    if val in column_set[c]:
                        return False
                    else:
                        column_set[c].add(val)
                    
                    box_idx = int(r/3)*3 + int(c/3)
                    print(box_idx)
                    if val in box_set[box_idx]:
                        return False
                    else:
                        box_set[box_idx].add(val)

        return True 
