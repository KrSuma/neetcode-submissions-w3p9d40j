class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # stack = []
        # res = 0

        # for p, s in zip(position, speed):
        #     x = (target - p) / s
        #     while stack and x == stack[-1]:
        #         res += 1
        #         stack.pop()
        #         x = 0
        #     if x:
        #         stack.append(x)
        # return res

        pair = [[p, s] for p, s in zip(position, speed)]
        pair.sort(reverse=True)

        stack = []

        for p, s in pair:
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)