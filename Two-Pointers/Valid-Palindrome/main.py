from sol import SolutionUsingWhile
from sol2 import SolutionUsingFor
from sol3 import SolutionMethod3


s1 = SolutionUsingWhile()
s2 = SolutionUsingFor()
s3 = SolutionMethod3()

test = "A man, a plan, a canal: Panama"

print(s1.isPalindrome(test))
print(s2.isPalindrome(test))
print(s3.isPalindrome(test))