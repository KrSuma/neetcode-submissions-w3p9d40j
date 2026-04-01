class MinStack:

    def __init__(self):
        self.s1 = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.s1.append(val)
        val = min(val, self.minstack[-1] if self.minstack else val)
        self.minstack.append(val)

    def pop(self) -> None:
        self.s1.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.s1[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
