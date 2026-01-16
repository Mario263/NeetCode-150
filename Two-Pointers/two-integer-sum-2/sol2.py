from typing import List

class SolutionUsingFor:
    def twoSum2(self, nums: List[int], target: int) -> List[int]: # type: ignore
        seen = {}
        for i, x in enumerate(nums):
            diff = target - x
            if diff in seen:
                return [seen[diff], i+1]
            seen[x]=i+1
        return []
        