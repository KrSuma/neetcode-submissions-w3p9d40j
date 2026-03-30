class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        l, r = 0, len(numbers) - 1

        while l < r:
            diff = numbers[r] + numbers[l]
            if target > diff:
                l += 1
            elif target < diff:
                r -= 1
            else:
                return [l+1, r+1]
        return []
