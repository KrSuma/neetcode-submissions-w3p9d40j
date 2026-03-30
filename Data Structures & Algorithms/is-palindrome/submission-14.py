class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        clean = []
        for letter in s:
            if letter.isalnum():
                clean.append(letter.lower())
        
        l, r = 0, len(clean) - 1
        while l < r:
            if clean[l] != clean[r]:
                return False
            l += 1
            r -= 1
        
        return True