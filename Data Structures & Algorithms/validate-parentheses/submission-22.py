class Solution:
    def isValid(self, s: str) -> bool:
        
        hashmap = {')':'(', ']':'[', '}':'{'}
        stack = []

        for char in s:
            if char in hashmap and stack and stack[-1] == hashmap[char]:
                    stack.pop()
            else:
                stack.append(char)
        
        return True if not stack else False
            
