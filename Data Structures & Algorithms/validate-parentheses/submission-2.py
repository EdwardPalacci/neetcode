class Solution:
    def isValid(self, s: str) -> bool:
        matching = {')': '(', '}': '{', ']': '['}
        stack = []

        for char in s:
            if char in matching:
                # It's a closing bracket: check top of stack
                top = stack.pop() if stack else None
                if top != matching[char]:
                    return False
            else:
                # It's an opening bracket
                stack.append(char)
        return len(stack) == 0