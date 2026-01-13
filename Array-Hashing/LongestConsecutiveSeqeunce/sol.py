from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int])-> int:
        num_set = set(nums)
        longest = 0
        for i in nums:
            if (i - 1) not in num_set:
                length = 0
                while(i + length) in num_set:
                    length+=1
                longest = max(length, longest)
        return longest
        
        
if __name__ == "__main__":
    print(Solution().longestConsecutive([2,20,4,10,3,4,5]))