class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        COLS = len(matrix[0])
        ROWS = len(matrix)
        l, r = 0, COLS * ROWS - 1

        while l <= r:
            m = (l + r) // 2
            col = m % COLS
            row = m // COLS

            if matrix[row][col] > target:
                r = m - 1
            elif matrix[row][col] < target:
                l = m + 1
            else:
                return True
        
        return False