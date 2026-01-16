from typing import List
from collections import defaultdict

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]: # type: ignore
        i,j = 0, len(numbers)-1
        while i<j:
            curr_sum = numbers[i] + numbers[j]
            if curr_sum<target:
                i+=1
            elif curr_sum>target:
                j-=1
            elif curr_sum == target:

                return [i+1,j+1]

