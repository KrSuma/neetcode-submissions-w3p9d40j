class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = []

        for c in s:
            if c == ']':
                res = ''
                while stack and stack[-1] != '[':
                    res = stack.pop() + res
                stack.pop() # remove '['
                num = ''
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                stack.append(int(num) * res)
            else:
                stack.append(c)

        return ''.join(stack)