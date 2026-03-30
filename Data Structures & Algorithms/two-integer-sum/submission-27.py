class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hashmap, key = diff, value = index

        hashmap = defaultdict(int)
        l = 0

        for r in range(len(nums)):
            if nums[r] in hashmap:
                return [hashmap[nums[r]], r]
            diff = target - nums[r]
            hashmap[diff] = r
        return []
