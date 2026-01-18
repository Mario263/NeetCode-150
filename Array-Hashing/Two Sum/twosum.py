from typing import List
class Solution:
    def twoSum(self, nums: list[int], target: int) -> List[int]:
        seen = {} # creating empty dictionary( a hash map )
        for i,x in enumerate(nums): # we are using enumerate cause we are dealing with both key and value pairs
            diff = target - x # calculating the difference between target and current number
            if diff in seen: # checking if the diff is already in the map, if not then we add the current numweber to the map
                return[seen[diff], i] # if found we return the indices of both the numbers
            seen[x]= i # adding the current number to the map with its index
        return List(seen.values()) #type: ignore
    
if __name__ == "__main__":
    print(Solution().twoSum([2,4,5,6,7,1,3], 9))
