from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        seen = []
        for i in strs:
            seen.append(str(len(i))+"#"+i)
        return "".join(seen)

    
    def decode(self, s: str) -> List[str]:
        res, i = [],0
        while i<len(s):
            j=1
            
            
        
if __name__ == "__main__":
    encoded = Solution().encode(["Hello", "World"])
    print("Encoded:", encoded)
    decoded = Solution().decode(encoded)
    print("Decoded:", decoded)