# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Time Complexity: O(n) | Space Complexity: O(1)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Setup the temporary variables
        prev, cur = None, head

        # Iterate through the entire list
        while(cur != None):
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node

        # Return the last node
        return prev
