class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        stack = []

        for i in s:
            if i in brackets:
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                else:
                    last_bracket = stack[-1]
                    if ((last_bracket != '(' and i == ')') or (
                            last_bracket != '{' and i == '}') or
                            (last_bracket != '[' and i == ']')):
                        return False
                    else:
                        stack.pop()
        return len(stack) == 0


# Concise solution
class Solution2:
    def isValid(self, s: str) -> bool:
        brackets = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        stack = []
        for i in s:
            if i in brackets:
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                elif i != brackets[stack.pop()]:
                    return False
        return len(stack) == 0
