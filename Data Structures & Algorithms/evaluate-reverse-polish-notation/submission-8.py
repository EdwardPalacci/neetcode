class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        my_stack = []
        for token in tokens:
            if token.lstrip("-").isdigit():
                my_stack.append(int(token))
            if token == "+":
                token1 = my_stack[-2]
                token2 = my_stack[-1]
                my_stack.pop()
                my_stack.pop()
                my_stack.append(token1 + token2)
            elif token == "-":
                token1 = my_stack[-2]
                token2 = my_stack[-1]
                my_stack.pop()
                my_stack.pop()
                my_stack.append(token1 - token2)
            elif token == "/":
                token1 = my_stack[-2]
                token2 = my_stack[-1]
                my_stack.pop()
                my_stack.pop()
                my_stack.append(int(token1 / token2))
            elif token == "*":
                token1 = my_stack[-2]
                token2 = my_stack[-1]
                my_stack.pop()
                my_stack.pop()
                my_stack.append(token1 * token2)
        return int(my_stack[0])