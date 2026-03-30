# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        # use slow and fast pointer

        slow, fast = head, head
        while fast and fast.next: # fast arrives at the end faster if theres an end of the list
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False