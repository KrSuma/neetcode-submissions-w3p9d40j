class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        counter = Counter(nums)
        majority = 0
        element = 0

        for k, v in counter.items():
            if v > majority:
                element = k
            majority = max(majority, v)
        return element
        