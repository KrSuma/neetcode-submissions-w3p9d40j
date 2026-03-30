class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        hashset = defaultdict(int)

        for n in nums:
            hashset[n] += 1
        majority = [0, 0]
        for n, cnt in hashset.items():
            if majority[1] < cnt:
                majority[0], majority[1] = n, cnt
        return majority[0]