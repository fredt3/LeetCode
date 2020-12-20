# 709. To Lower Case

class Solution:
    def toLowerCase(self, str: str) -> str:
        res = []
        for c in str:
            if ord("A") <= ord(c) and ord(c) <= ord("Z"):
                res.append(chr(ord(c) + 32))
            else:
                res.append(c)
        return "".join(res)


# output "hello, world!"
str = "Hello, World!"
print(Solution().toLowerCase(str))
