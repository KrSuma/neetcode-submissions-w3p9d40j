class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for t in tokens:
            if stack and t == '+':
                f = stack.pop()
                s = stack.pop()
                stack.append(s + f)
            elif stack and t == '-':
                f = stack.pop()
                s = stack.pop()
                stack.append(s - f)
            elif stack and t == '*':
                f = stack.pop()
                s = stack.pop()
                stack.append(s * f)
            elif stack and t == '/':
                f = stack.pop()
                s = stack.pop()
                stack.append(int(s / f))
            else:
                stack.append(int(t))

        return stack[-1]