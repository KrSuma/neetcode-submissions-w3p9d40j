class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        l, r = 0, len(numbers) - 1
        nums = numbers
        while l < r:
            if nums[r] + nums[l] > target:
                r -= 1
            elif nums[r] + nums[l] < target:
                l += 1
            else:
                return [l+1, r+1]
        
        return []