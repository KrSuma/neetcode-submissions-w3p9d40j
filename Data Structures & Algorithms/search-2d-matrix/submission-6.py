class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        COLS = len(matrix[0])
        ROWS = len(matrix) 
        l, r = 0, (COLS * ROWS) - 1

        while l <= r:
            m = (r + l) // 2
            cols = m % COLS
            rows = m // COLS

            if matrix[rows][cols] > target:
                r = m - 1
            elif matrix[rows][cols] < target:
                l = m + 1
            else:
                return True
        
        return False