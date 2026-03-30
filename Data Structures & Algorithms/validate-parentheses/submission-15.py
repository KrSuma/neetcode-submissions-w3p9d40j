class Solution:
    def isValid(self, s: str) -> bool:
        
        hashmap = {')':'(', ']':'[','}':'{',}
        res = []

        for char in s:
            if char in hashmap:
                if res and res[-1] == hashmap[char]:
                    res.pop()
                else:
                    return False
            else:
                res.append(char)
        
        return True if not res else False