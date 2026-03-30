class Solution:
    def isValid(self, s: str) -> bool:

        pairs = {')':'(', ']':'[', '}':'{'}
        stack = []

        for char in s:
            if char in pairs:
                if stack and pairs[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        return False if stack else True