# 559. Maximum Depth of N-ary Tree

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0

        depth = [0]
        for child in root.children:
            depth.append(self.maxDepth(child))

        return max(depth) + 1
