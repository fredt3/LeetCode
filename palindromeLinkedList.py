# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def isPalindrome(self, head):
        slow = head
        fast = head
        while fast:
            if fast.next == None:
                break
            fast = fast.next.next
            slow = slow.next

        slow = self.reverseList(slow)
        fast = head

        while(slow != None):
            if(slow.val != fast.val):
                return False
            slow = slow.next
            fast = fast.next

        return True

    def reverseList(self, head):
        prev = None
        while head:
            nextNode = head.next
            head.next = prev
            prev = head
            head = nextNode
        return prev
