from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for i in nums:
            if i not in seen:
                seen[i] = 0
            seen[i]+= 1
        return [x[0] for x in sorted(seen.items(), key=lambda x: x[1], reverse=True)[:k]]


if __name__ == "__main__":
    print(Solution().topKFrequent([1,2,3,4,3,2], 2))
        