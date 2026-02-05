class Solution:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self)-> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self)-> int:
        return self.stack[-1]

    def getMin(self)-> int:
        return self.minStack[-1]
    

if __name__ == "__main__":
    s = Solution()
    s.push(3)
    s.push(5)
    print("min:", s.getMin())
    s.push(2)
    s.push(1)
    print("min:", s.getMin())
    s.pop()
    print("top:", s.top())
    print("min:", s.getMin())