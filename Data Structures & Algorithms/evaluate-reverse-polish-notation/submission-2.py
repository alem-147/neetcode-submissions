import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        result = 0

        def pop_vals() -> tuple[int, int]:
            b = stack.pop()
            a = stack.pop()
            return a, b

        for t in tokens:
            match t:
                case "-":
                    a, b = pop_vals()
                    stack.append(a-b)
                case "+":
                    a, b = pop_vals()
                    stack.append(a+b)
                case "*":
                    a, b = pop_vals()
                    stack.append(a*b)
                case "/":
                    a, b = pop_vals()
                    stack.append(int(a/b))
                case _:
                    stack.append((int(t)))
        return stack[-1]