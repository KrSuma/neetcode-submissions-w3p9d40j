class MinStack:

    def __init__(self):
        self.s = []
        self.minstack = []

    def push(self, val: int) -> None:
        if self.minstack:
            if self.minstack[-1] <= val:
                self.minstack.append(self.minstack[-1])
            else:
                self.minstack.append(val)
        else:
            self.minstack.append(val)
        self.s.append(val)
        

    def pop(self) -> None:
        self.s.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
