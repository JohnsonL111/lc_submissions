# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr = head
        curr = head
        prev = None

        while curr:
            # update ptrs
            nextNode = curr.next
            curr.next = prev

            # update prev and curr
            prev = curr
            curr = nextNode

        return prev