from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        freq = [[] for i in range(len(nums)+1)]
        
        for i in nums:
            seen[i] = seen.get(i,0) + 1
        for i,n in seen.items():
            freq[n].append(i)
        res = []
        
        for i in range(len(freq)-1,0,-1):
            for c in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        
if __name__ == "__main__":
    print(Solution().topKFrequent([1,2,3,4,3,2], 2))
        