from typing import List
# there are three ways by which this question can be solved 
# i am using the best optimized setting to solve this problem
# I will be using a hash set to keep track of the elemnts we have seen so far,
# and check if the current element is already in the set. 

class Solution:
    def hasDuplicate(self, nums: List[int])-> bool:
        seen = set() # Initialize an empty hash set to store elements we have encountered
        for i in nums: # Iterate through each number 'i' in the input list 'nums'
            if i in seen: # Check if the current number 'i' is already in the set
                return True # If it is, we found a duplicate, so return True
            seen.add(i) # Add 'i' to the set to track it for future checks
        return False # If the loop completes without finding duplicates, return False

if __name__ == "__main__":
    # Instantiate the Solution class
    solution = Solution()

    # Define test cases
    test_cases = [
        [1, 2, 3, 3],  # Expected: True
        [1, 2, 3, 4]   # Expected: False
    ]

    # Run the function for each test case and print the result
    for nums in test_cases:
        result = solution.hasDuplicate(nums)
        print(f"Input: {nums} -> Output: {result}")
        