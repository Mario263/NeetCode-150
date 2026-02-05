from sol import Solution

def main():
    s = Solution()
    actions = [
        ("push", 3),
        ("push", 5),
        ("getMin", None),
        ("push", 2),
        ("push", 1),
        ("getMin", None),
        ("pop", None),
        ("top", None),
        ("getMin", None),
    ]

    for act, val in actions:
        if act == "push":
            s.push(val)
            print(f"push({val})")
        elif act == "pop":
            s.pop()
            print("pop()")
        elif act == "top":
            print("top ->", s.top())
        elif act == "getMin":
            print("getMin ->", s.getMin())


if __name__ == "__main__":
    main()
