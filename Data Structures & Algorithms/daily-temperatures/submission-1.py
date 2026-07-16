class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        tempdays=[0]*len(temperatures)
        for i,temp in enumerate(temperatures):
            while stack and temp>stack[-1][-1]:
                day=stack.pop()
                tempdays[day[0]]=i-day[0]
            stack.append((i,temp))
        return tempdays
