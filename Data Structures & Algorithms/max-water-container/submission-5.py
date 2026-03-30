class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l, r = 0, len(heights) - 1
        max_amount = 0

        while l < r:
            width = r - l 
            height = min(heights[l], heights[r])
            amount = width * height
            max_amount = max(max_amount, amount)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        
        return max_amount