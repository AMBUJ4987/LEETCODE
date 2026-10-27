# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
     
 
        d = ListNode(0)
        curr = d
        c = 0
        while l1 or l2 or c:
            t = c
            if l1:
                t += l1.val
                l1 = l1.next
            if l2:
                t+= l2.val
                l2 = l2.next
            c = t//10
            curr.next = ListNode(t%10)
            curr = curr.next
        return d.next