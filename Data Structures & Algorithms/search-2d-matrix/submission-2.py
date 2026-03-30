class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        l, r = 0, (cols * rows) - 1 # treat the 2d matrix like a single 1d

        while l <= r:
            m = (l + r) // 2

            # conversion
            row = m // cols
            col = m % cols
            mid = matrix[row][col]

            if mid > target:
                r = m - 1
            elif mid < target:
                l = m + 1
            else:
                return True

        return False