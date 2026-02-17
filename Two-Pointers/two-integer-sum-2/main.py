from sol import Solution
from sol2 import SolutionUsingFor


c1 = Solution()
c2 = SolutionUsingFor()

nums = [2,4,6]
target = 6

print(c1.twoSum(nums, target))
print(c2.twoSum2(nums, target)