class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        stack = []

        for o in operations:
            if o == '+':
                if stack:
                    stack.append(stack[-1] + stack[-2])
            elif o == 'D':
                if stack:
                    stack.append(stack[-1] * 2)
            elif o == 'C':
                if stack:
                    stack.pop()
            else:
                stack.append(int(o))
        
        return sum(stack)