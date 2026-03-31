class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for t in tokens:
            if t == '+':
                if stack:
                    first = stack.pop()
                    second = stack.pop()
                    stack.append(second + first)
            elif t == '-':
                if stack:
                    first = stack.pop()
                    second = stack.pop() 
                    stack.append(second - first)
            elif t == '*':
                if stack:
                    first = stack.pop()
                    second = stack.pop()
                    stack.append(second * first)
            elif t == '/':
                if stack:
                    first = stack.pop()
                    second = stack.pop()
                    stack.append(int(second / first))
            else:
                stack.append(int(t))
        
        return stack[-1]