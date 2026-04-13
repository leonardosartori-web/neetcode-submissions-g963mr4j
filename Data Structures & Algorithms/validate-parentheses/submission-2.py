class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closing_parenthesis = {
            "(": ")",
            "[": "]",
            "{": "}"
        }

        for c in s:
            if c in closing_parenthesis:
                stack.append(c)
            else:
                if stack:
                    opened = stack[-1]
                    if c == closing_parenthesis[opened]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        return not stack