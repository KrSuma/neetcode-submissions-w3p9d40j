class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        joined = ''.join([c for c in s if c.isalnum()]).lower()

        l, r = 0, len(joined) - 1

        while l < r:
            if joined[l] != joined[r]:
                return False
            else:
                l += 1
                r -= 1
        
        return True