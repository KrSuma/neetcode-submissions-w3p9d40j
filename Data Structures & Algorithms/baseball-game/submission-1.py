class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for op in operations:
            if op == '+':
                first, second = stack[-1], stack[-2]
                res = first + second
                stack.append(res)
            elif op == 'D':
                first = stack[-1]
                res = first * 2
                stack.append(res)
            elif op == 'C':
                stack.pop()
            else:
                stack.append(int(op))
        
        return sum(stack)