class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set(nums)
        output = 0

        for n in hash_set:
            if (n - 1) not in hash_set:
                current_num = n
                current_streak = 1

                while (current_num + 1) in hash_set:
                    current_num += 1
                    current_streak += 1
                    
                output = max(current_streak, output)

        return output
                