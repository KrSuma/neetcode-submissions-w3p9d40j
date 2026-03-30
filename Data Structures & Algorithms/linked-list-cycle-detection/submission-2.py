# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # hash_set = set()
        # node = head

        # while node:
        #     if node in hash_set:
        #         return True
        #     hash_set.add(node)
        #     node = node.next
        # return False

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
                
        return False

