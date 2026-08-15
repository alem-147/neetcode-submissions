class MinStack:

    def __init__(self):
        self.stk = []
        self.min_stk = []

    def push(self, val: int) ->  None:
        if self.min_stk:
            self.min_stk.append(min(val, self.min_stk[-1]))
        else:
            self.min_stk.append(val)
        self.stk.append(val)

    def pop(self) -> None:
        self.stk.pop()
        self.min_stk.pop()

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.min_stk[-1]