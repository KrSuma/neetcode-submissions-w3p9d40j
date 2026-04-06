class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        stack = []

        for o in operations:
            if stack and o == '+':
                first = stack[-1]
                second = stack[-2]
                stack.append(first + second)
            elif stack and o == 'D':
                first = stack[-1]
                stack.append(first * 2)
            elif stack and o == 'C':
                stack.pop()
            else:
                stack.append(int(o))
        
        return sum(stack)