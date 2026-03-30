class Solution:
    def isPalindrome(self, s: str) -> bool:
        # cleaned = ''.join(s).lower()
        cleaned = ''.join(c for c in s.lower() if c.isalnum())

        l, r = 0, len(cleaned)-1
        while l <= r:
            if cleaned[l] == cleaned[r]:
                l += 1
                r -= 1
            else:
                return False
        return True