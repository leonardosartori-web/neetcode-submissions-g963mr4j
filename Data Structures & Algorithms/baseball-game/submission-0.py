class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stk = deque()
        for o in operations:
            if o == "+":
                stk.append(stk[-1] + stk[-2])
            elif o == "D":
                stk.append(stk[-1] * 2)
            elif o == "C":
                stk.pop()
            else:
                stk.append(int(o))
        return sum(stk)