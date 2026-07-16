class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for el in tokens:
            if el in "+-*/":
                op = el
                a=int(stack.pop())
                b=int(stack.pop())
                if op=="+":
                    stack.append(a+b)
                elif op=="-":
                    stack.append(b-a)
                elif op=="*":
                    stack.append(a*b)
                elif op=="/":
                    if b==0:
                        stack.append(0)
                    else:
                        stack.append(int(b/a))
            else:
                stack.append(int(el))
        return int(stack[0])
                
