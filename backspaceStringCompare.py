# 844. Backspace String Compare

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def helper(s):
            stack = []
            for c in s:
                if c != "#":
                    stack.append(c)
                elif stack:
                    stack.pop()
            return "".join(stack)

        return helper(S) == helper(T)


# Ouput: True
S = "y#fo##f"
T = "y#f#o##f"
print(Solution().backspaceCompare(S, T))
