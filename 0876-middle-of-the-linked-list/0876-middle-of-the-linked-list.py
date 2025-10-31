# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s, f = ListNode(0, head), ListNode(0, head)

        while f:
            s = s.next
            if f.next and f.next.next:
                f = f.next.next
            else:
                break

        return s
        