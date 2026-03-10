from typing import List

from containsDuplicate import Solution


a = Solution()


def main():
    test_cases = [[1,2,3,4,5], [1,2,2,3,4,4]]
    return test_cases

if __name__=="__main__":
    for num in main():
        res = a.hasDuplicate(num)
        print(f"{num} -> {res}")