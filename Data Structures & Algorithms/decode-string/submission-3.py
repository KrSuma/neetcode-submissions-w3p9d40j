class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = []

        for c in s:
            if c == ']':
                res = ''
                while stack and stack[-1] != '[':
                    res = stack.pop() + res
                stack.pop()

                digit = ''
                while stack and stack[-1].isdigit():
                    digit = stack.pop() + digit
                stack.append(int(digit) * res)
            else:
                stack.append(c)
        
        return ''.join(stack)