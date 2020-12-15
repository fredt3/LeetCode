"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def postorder(self, root):
        output = []
        if(root == None):
            return output

        stack = [root]

        while stack:
            node = stack.pop()
            output.insert(0, node.val)
            for child in node.children:
                stack.append(child)

        return output
