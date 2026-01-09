from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        seen = []
        for i in range(len(strs)):
            seen.append(str(len(strs[i]))+"#"+(strs[i]))
        return "".join(seen)
    
    def decode(self, s: str) -> List[str]:
        res,i = [], 0
        while i<len(s):
            j = i
            while s[j]!="#":
                j+=1
            leng = int(s[i:j])
            res.append(s[j+1:j+1+leng])
            i = j+1+leng
        return res
        
if __name__ == "__main__":
    encoded = Solution().encode(["Hello", "World"])
    print("Encoded:", encoded)
    decoded = Solution().decode(encoded)
    print("Decoded:", decoded)