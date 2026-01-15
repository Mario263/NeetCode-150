class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
        # skip non-alphanumeric on left
            while i < j and not s[i].isalnum():
                i += 1
        # skip non-alphanumeric on right
            while i < j and not s[j].isalnum():
                j -= 1
        
            if s[i].lower() != s[j].lower():
                return False
        
            i += 1
            j -= 1
    
        return True

if __name__ == "__main__":
    print(Solution().isPalindrome("poop"))