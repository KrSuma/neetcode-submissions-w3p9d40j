class Solution:
    def isPalindrome(self, s: str) -> bool:
        # first, we remove spaces and non-alpha chars

        string = ' '.join(s).lower()
        clean = ''
        for s in string:
            if s.isalnum():
                clean += s
        
        l, r = 0, len(clean) - 1
        while l < r:
            if clean[l] == clean[r]:
                l += 1
                r -= 1
            else:
                return False
        return True