class SolutionMethod3:
    def isPalindrome(self,s:str)-> bool:
        i,j = 0, len(s) - 1

        while i<j:
            while i < j and not self.album(s[i]): # type: ignore
                i+=1
            while i<j and not self.album(s[j]): # type: ignore
                j-=1

            if s[i].lower() != s[j].lower():
                return False
            i+=1
            j-=1
        return True

    def album(self, c):
        return (ord("A") <= ord(c) <= ord("Z") 
                or (ord('a') <= ord(c) <= ord('z'))

                or (ord('0') <= ord(c) <= ord('9')))
