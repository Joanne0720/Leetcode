class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in {'+', '-', '*', '/'}:
                a, b = stack.pop(), stack.pop()
                token = str(int(eval(b + token + a)))
            stack.append(token)
        return stack[0]