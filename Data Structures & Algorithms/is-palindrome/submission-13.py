class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        clean = []

        for char in s:
            if char.isalnum():
                clean.append(char.lower())
        
        l, r = 0, len(clean) - 1
        while l < r:
            if clean[l] != clean[r]:
                return False
            l += 1
            r -= 1

        return True