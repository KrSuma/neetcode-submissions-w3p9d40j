class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        prefix = []
        total = 0
        for n in nums:
            total += n
            prefix.append(total)
        
        postfix = deque()
        total = 0
        for i in range(len(nums)-1, -1, -1):
            total += nums[i]
            postfix.appendleft(total)

        # which index is the pivot index

        for i in range(len(nums)):
            if prefix[i] == postfix[i]:
                return i
        
        return -1