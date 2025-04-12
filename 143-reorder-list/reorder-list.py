# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # use tortoise and hare
        # by the time hare gets to the end of the LL
        # the tortoise is at the center
        # split into two lists first and 2nd half
        # sequentially add the first node of the first half and the first node of the reversed 2nd half
        # ex: 1-2-3-4-5
        # ans: 1-5-2-4-3

        # slow: 1-2-3

        # first half: 1-2-3
        # 2nd half: 4-5
        # 1-5-2-4-3
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        if not head or not head.next:
            return

        # Step 1: Find middle using tortoise and hare
        t = head
        h = head
        prev = None

        while h and h.next:
            prev = t
            t = t.next
            h = h.next.next

        # Break the list into two halves
        if prev:
            prev.next = None

        first = head
        second = t

        # Step 2: Reverse the second half
        prev = None
        curr = second

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        second = prev  # new head of reversed second half

        # Step 3: Merge the two halves
        while first and second:
            temp1 = first.next
            temp2 = second.next

            first.next = second

            # Only set second.next if temp1 exists
            if temp1:
                second.next = temp1

            first = temp1
            second = temp2




        


        