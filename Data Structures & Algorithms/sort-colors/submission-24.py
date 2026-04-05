class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        l = 0
        r = len(nums) - 1

        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]

        index = 0
        while index <= r:
            if nums[index] == 0:
                swap(l, index)
                l += 1
            elif nums[index] == 2:
                swap(index, r)
                r -= 1
                index -= 1
            index += 1
