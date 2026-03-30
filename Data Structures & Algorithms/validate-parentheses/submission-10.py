class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        closing = {')':'(', ']':'[', '}':'{'}

        for bracket in s:
            if bracket not in closing:
                stack.append(bracket)
            elif bracket in closing:
                if stack and closing[bracket] == stack[-1]:
                    stack.pop()
                else:
                    return False

        return True if not stack else False
                