class Solution:
    def isAnagram(self, s: str, t: str) -> bool: # we have two strings s and t, the expected output is in the boolean format
        if len(s) != len(t): # we check if the length of both the strings are equal or not
            return False # if not equal we return false
        return sorted(s)==sorted(t) # we retuen the comparison of both the strings after sorting them
                
if __name__ == "__main__":
    print(Solution().isAnagram("anagram","nagaram"))
    
 # sorted    
#  sorted(s) turns the string into a list of its characters in increasing order, and sorted(t) does the same for t.

# If s = "anagram" and t = "nagaram", both become ['a','a','a','g','m','n','r'] after sorting.
# return sorted(s) == sorted(t) checks whether these two sorted lists are exactly the same; if they are, every character appears the same number of times in both strings, so they are anagrams.