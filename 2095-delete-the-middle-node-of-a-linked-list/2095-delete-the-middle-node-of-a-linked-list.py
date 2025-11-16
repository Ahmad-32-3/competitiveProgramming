# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        r = head
        l = ListNode(0, head)
        slow = l

        while r and r.next:
            slow = slow.next
            r = r.next.next
        slow.next = slow.next.next
        
            
        return l.next
        