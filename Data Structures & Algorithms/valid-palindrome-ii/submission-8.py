class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        l, r = 0, len(s) - 1

        def check(s):
            l, r = 0, len(s) -1
            while l < r:
                if s[l] != s[r]:
                    return False
                else:
                    l += 1
                    r -= 1
            return True

        while l < r:
            if s[l] != s[r]:
                return check(s[l+1:r+1]) or check(s[l:r])
            else:
                l += 1
                r -= 1    
        return True