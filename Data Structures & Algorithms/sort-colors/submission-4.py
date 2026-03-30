class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # solution 1 - Counting sort
        count = [0] * 3
        for n in nums:
            count[n] += 1

        index = 0
        for i in range(3):
            while count[i]:    
                count[i] -= 1
                nums[index] = i
                index += 1 

        # solution 2 - Three pointers
        l, r = 0, len(nums) - 1
        i = 0

        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]
        
        while i <= r:
            if nums[i] == 0:
                swap(l, i)
                l += 1
            elif nums[i] == 2:
                swap(i, r)
                r -= 1
                i -= 1
            i += 1

