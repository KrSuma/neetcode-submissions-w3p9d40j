class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def isvalid(s):
            l, r = 0, len(s) - 1
            while l <= r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        l, r = 0, len(s) - 1
        while l <= r:
            if s[l] != s[r]:
                return isvalid(s[l:r]) or isvalid(s[l+1:r+1])
            l += 1
            r -= 1

        return True
