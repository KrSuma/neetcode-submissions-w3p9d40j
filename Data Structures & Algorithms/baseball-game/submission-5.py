class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for c in operations:
            if c == '+':
                if stack: 
                    stack.append(stack[-1] + stack[-2])
            elif c == 'D':
                if stack:
                    stack.append(stack[-1] * 2)
            elif c == 'C':
                if stack:
                    stack.pop()
            else:
                stack.append(int(c))
        
        return sum(stack)