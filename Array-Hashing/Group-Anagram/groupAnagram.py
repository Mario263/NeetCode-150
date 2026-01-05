# from typing import List
# from collections import defaultdict

# class Solution:
#     def validAnagram(self, strs: List[str]) -> List[List[str]]:
#         res = defaultdict(list)
        
#         for s in strs:
#             count = [0] * 26
#             for c in s:
#                 count[ord(c) - ord("a")] += 1
#             res[tuple(count)].append(s)
#         return list(res.values())
from typing import List
from collections import defaultdict

class Solution:
    def validAnagram(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                co = ord(c) - ord("a")
                count[co]+=1
            key = tuple(count)
            seen[key].append(s)
        return list(seen.values())
                
        
        
 

if __name__ == "__main__":
     print(Solution().validAnagram(["act", "pots", "tops", "stop", "cat", "hat"]))