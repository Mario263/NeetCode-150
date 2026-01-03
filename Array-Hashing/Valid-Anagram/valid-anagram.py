class Solution:
    def isAnagram(self, s: str, t: str) -> bool: # we have two strings s and t, the expected output is in the boolean format
        if len(s) != len(t): # we check if the length of both the strings are equal or not
            return False # if not equal we return false
        return sorted(s)==sorted(t) # we retuen the comparison of both the strings after sorting them
                
if __name__ == "__main__":
    print(Solution().isAnagram("anagram","nagaram"))