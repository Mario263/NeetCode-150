from typing import List

class Solution:
    def dailyTemp(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures)
        stack = [] # index, temp
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                print(stack[-1][0])

                stackT, stackInd = stack.pop()

                result[stackInd] = (i - stackInd)
            stack.append([t,i])
        return result 
        
        
