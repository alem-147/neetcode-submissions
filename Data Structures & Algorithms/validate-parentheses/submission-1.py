
class Solution:
    def isValid(self, s: str) -> bool:
        """
        Stack

        Deal with most recent bracket type before dealing with earlier ones
        """
        stack = []


        for b in s:
            match b:
                case b if b in "[{(":
                    stack.append(b)
                case "]":
                    if not stack or stack[-1] != "[":
                        return False
                    stack.pop()
                case ")":
                    if not stack or stack[-1] != "(":
                        return False
                    stack.pop()
                case "}":
                    if not stack or stack[-1] != "{":
                        return False
                    stack.pop()
                case _:
                    continue
        
        return not stack
                
        