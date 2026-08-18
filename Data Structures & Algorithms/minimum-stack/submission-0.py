class MinStack:

    def __init__(self):
        self.stack = []
        self.min = sys.maxsize

    def push(self, val: int) -> None:
        self.stack.append((val, self.min))
        if val < self.min:
            self.min = val

    def pop(self) -> None:
        if self.stack:
            top = self.stack.pop()
            self.min = top[1]

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]

    def getMin(self) -> int:
        if self.stack:
            return self.min
        
