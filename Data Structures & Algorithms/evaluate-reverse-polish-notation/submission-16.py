class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        vals=["+","*","/","-"]
        for c in tokens:

            if c=="+":
                stack.append(stack.pop()+stack.pop())
            elif c=="*":
                stack.append(stack.pop()*stack.pop())
            elif c=="-":
                p1=int(stack.pop())
                p2=int(stack.pop())
                res=p2-p1
                stack.append(res)
            elif c=="/":
                p1=stack.pop()
                p2=stack.pop()
                res=int(float(p2)/p1)
                stack.append(res)
            else:
                stack.append(int(c))


       
        return stack[0]


            