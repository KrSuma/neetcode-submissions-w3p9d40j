# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        leftprev = dummy
        curr = head

        # reach node a postion 'left'
        for i in range(left - 1):
            leftprev = curr
            curr= curr.next

        # reverse until we reach 'right'
        prev = None
        for i in range(right - left + 1):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # update pointers
        leftprev.next.next = curr
        leftprev.next = prev
        return dummy.next
        

        

