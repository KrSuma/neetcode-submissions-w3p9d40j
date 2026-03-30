class Solution:
    def isValid(self, s: str) -> bool:
        
        bracket = { ')':'(', '}':'{', ']':'[',}
        stack = []

        for c in s:
            if c in bracket and stack and stack[-1] == bracket[c]:
                stack.pop()
            else:
                stack.append(c)

        return True if not stack else False 