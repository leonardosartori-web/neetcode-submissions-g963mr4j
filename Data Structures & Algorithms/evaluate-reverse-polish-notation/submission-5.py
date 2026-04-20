class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stk = deque()

        for tkn in tokens:

            if tkn == "+":
                stk.append(stk.pop() + stk.pop())
            elif tkn == "-":
                stk.append(-1*(stk.pop() - stk.pop()))
            elif tkn == "*":
                stk.append(stk.pop() * stk.pop())
            elif tkn == "/":
                a, b = stk.pop(), stk.pop()
                stk.append(int(float(b)/a))
            else:
                stk.append(int(tkn))

        return stk[0]           
