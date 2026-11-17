import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        symbol = ['+', '-', '*', '/']
        stack = []
        res = 0

        if len(tokens) <= 1:
            return int(tokens[0])

        for token in tokens: 
            if token not in symbol:
                stack.append(token)
            else:
                top1 = int(stack.pop())
                top2 = int(stack.pop())
                if token == "+":
                    res = top2 + top1
                    stack.append(res)
                elif token == "-":
                    res = top2 - top1
                    stack.append(res)
                elif token == "*":
                    res = top2 * top1
                    stack.append(res)
                elif token == "/":
                    res = math.trunc(top2 / top1)
                    stack.append(res)
               
        return stack[0]
