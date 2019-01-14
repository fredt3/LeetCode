# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ans = ansHead = ListNode(0)
        while(l1 or l2):
            if(l1):
                ans.val += l1.val
                l1 = l1.next
            if(l2):
                ans.val += l2.val
                l2 = l2.next
            
            if(ans.val > 9):
                ans.val -= 10
                ans.next = ListNode(1)
                ans = ans.next
            if(l1 or l2):
                ans.next = ListNode(0)
                ans = ans.next  
        return ansHead