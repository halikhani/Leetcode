# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        # calculate total len of the list
        
        list_len = 0
        current = head
        
        while current != None:
            list_len += 1
            current = current.next
        
        # calculate number of steps to go forward to reach the new head
        steps = list_len - k
        
        # change the head and change next pointers
        left_side_head = head
        right_side = head
        
        counter = steps
        current = head
        while counter != 0:
            right_side = right_side.next
            counter -= 1
        
        # concatenate
        
        
        
        