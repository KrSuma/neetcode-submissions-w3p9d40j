class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        res = 0

        for t in tokens:
            if t == '+' and stack:
                first, second = stack.pop(), stack.pop()
                stack.append(first + second)
            elif t == '*' and stack:
                first, second = stack.pop(), stack.pop()
                stack.append(first * second)
            elif t == '/':
                first, second = stack.pop(), stack.pop()
                stack.append(int(second / first))
            elif t == '-':
                first, second = stack.pop(), stack.pop()
                stack.append(second - first)
            else:
                stack.append(int(t))
        
        return stack[0]
        
