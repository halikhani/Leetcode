# Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

# Example 1:

# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]


# Example 2:

# Input: head = [1], n = 1
# Output: []


# Example 3:

# Input: head = [1,2], n = 1
# Output: [1]
 

# Constraints:

# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        if head is None:
            return head
        
        current = head
        prev = None
        count = 0
        # counting the nodes in the list
        while current is not None:
            count += 1
            current = current.next

        current = head
        target = count - (n-1)
        i = 1
        while current is not None:
            if i == target :
                if prev is None:
                    return current.next
                else:
                    prev.next = current.next
                    return head
            else:
                nxt = current.next
                prev = current
                current = nxt
                i += 1         