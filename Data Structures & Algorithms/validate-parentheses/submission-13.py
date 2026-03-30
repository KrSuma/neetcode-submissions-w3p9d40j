class Solution:
    def isValid(self, s: str) -> bool:
        
        check = {
            ')':'(',
            ']':'[',
            '}':'{',
        }

        stack = []

        for char in s:
            if char in check: 
                if stack and check[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return True if not stack else False 