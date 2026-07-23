# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        first = head

        for _ in range(k - 1):
            first = first.next

        kth_from_start = first

        second = head
        while first.next:
            first = first.next
            second = second.next

        kth_from_start.val, second.val = second.val, kth_from_start.val

        return head