from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # seen: maps each number -> how many times it appears in nums
        seen = {}
        # freq: index = frequency, value = list of numbers with that frequency
        # size is len(nums)+1 because max frequency of any number is len(nums)
        freq = [[] for i in range(len(nums)+1)]

        # count how many times each number appears
        for i in nums:
            # get current count of i (default 0), add 1, store back
            seen[i] = seen.get(i,0) + 1

        # fill buckets: for each (number, count), put number into bucket at index = count
        for i, c in seen.items():
            freq[c].append(i)

        # res will store the answer: the k most frequent numbers
        res = []
        # iterate frequencies from highest (end of freq) down to 1
        for i in range(len(freq)-1, 0, -1):
            # for this frequency i, look at all numbers that appear i times
            for c in freq[i]:
                # take this number into the result
                res.append(c)
                # once we have k numbers, we can return
                if len(res) == k:
                    return res

        
if __name__ == "__main__":
    print(Solution().topKFrequent([1,2,3,4,3,2], 2))
        