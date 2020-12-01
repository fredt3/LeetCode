# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = ans = ListNode("")

        while(l1 or l2):
            if(l1 and l2):
                if(l1.val < l2.val):
                    l3.val = l1.val
                    print(l3.val)
                    l1 = l1.next
                    if(l1 or l2):
                        l3.next = ListNode("")
                        l3 = l3.next
                else:
                    l3.val = l2.val
                    print(l3.val)
                    l2 = l2.next
                    if(l1 or l2):
                        l3.next = ListNode("")
                        l3 = l3.next

            if(l1 and not l2 or l1.val < l2.val):
                l3.val = l1.val
                print(l3.val)
                l1 = l1.next
                if(l1 or l2):
                    l3.next = ListNode("")
                    l3 = l3.next
            if(l2 and not l1 or l1.val > l2.val):
                l3.val = l2.val
                print(l3.val)
                l2 = l2.next
                if(l1 or l2):
                    l3.next = ListNode("")
                    l3 = l3.next

        return ans
