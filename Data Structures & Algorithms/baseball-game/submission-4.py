class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for s in operations:
            if s == '+':
                if stack:
                    first = stack[-1]
                    second = stack[-2]
                    stack.append((first + second))
            elif s == 'C':
                if stack:
                    stack.pop()
            elif s == 'D':
                if stack:
                    first = stack[-1]
                    stack.append((first * 2))
            else:
                stack.append(int(s))
        return sum(stack)