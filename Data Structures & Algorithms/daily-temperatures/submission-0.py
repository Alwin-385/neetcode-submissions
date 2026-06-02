class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack =[]
        for i ,t in enumerate(temperatures):
            while stack and t>stack[-1][0]:
                stackt,stackindx=stack.pop()
                res[stackindx]=i-stackindx
            stack.append((t,i))
        return res        
                
            



        