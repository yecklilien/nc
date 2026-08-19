class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        len_row = len(matrix)
        len_column = len(matrix[0])
        left = 0
        right = len_row * len_column - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            mid_value = self.getValue(mid, matrix, len_column)
            if mid_value == target:
                return True
            
            if target < mid_value :
                right = mid - 1
            if target > mid_value:
                left = mid + 1
        
        return False

    
    def getValue(self, index: int, matrix: List[List[int]], len_column: int) -> int:
        r = index // len_column
        c = index % len_column
        return matrix[r][c]


    