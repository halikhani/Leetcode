# You are given the head of a singly linked-list. The list can be represented as:

# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:

# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.


# Example 1:

# Input: head = [1,2,3,4]
# Output: [1,4,2,3]


# Example 2:

# Input: head = [1,2,3,4,5]
# Output: [1,5,2,4,3]
 

# Constraints:

# The number of nodes in the list is in the range [1, 5 * 10^4].
# 1 <= Node.val <= 1000

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
        # got help from neetcode for this
        # first find the middle node
        slow, fast = head, head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reversing the second half (start node is slow)
        second = slow.next
        
        # separating the first and second half of the linked list
        slow.next = None
        
        # defining the prev for reversing the second half
        prev = None
        
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
            
            
        # finally, merge the two halves.
        # the new head of the reversed of the second half is prev
        second = prev
        first = head
        # we know that the second half is always shorter than the first half
        while second:
            tmp_f, tmp_s = first.next, second.next
            first.next = second
            second.next = tmp_f
            first, second = tmp_f, tmp_s
            