class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0

        if len(heights) < 1:
            return 0 

        i, j = 0, len(heights) - 1
        while i < j:
            length = j - i
            height = min(heights[i], heights[j])
            area = length * height
            max_area = max(area, max_area)
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1

        return max_area
