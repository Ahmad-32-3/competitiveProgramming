# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        r = head
        l = ListNode(0, head)
        counter = 0
        ork = head
        while ork:
            ork = ork.next
            counter += 1
        while r.next and r.next.next:
            l = l.next
            r = r.next.next
        if counter == 1:
            return [ListNode]
        if counter % 2 == 1:
            l.next = l.next.next
        else:
            l.next.next = l.next.next.next
            
        return head
        