import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        result = 0

        for t in tokens:
            if t.isalnum() or (t[0] == "-" and t[0] != t[-1]):
                stack.append(int(t))
            else:
                b = stack.pop()
                a = stack.pop()
                if t in "+":
                    result = a + b
                elif t in "-":
                    result = a - b
                elif t in "*":
                    result = a * b
                else:
                    result = int(a/b)
                stack.append(result)
        return stack[-1]