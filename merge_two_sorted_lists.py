# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

# Example 3:
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# Example 2:
# Input: list1 = [], list2 = []
# Output: []

# Example 3:
# Input: list1 = [], list2 = [0]
# Output: [0]

# Constraints:
# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        first_node = ListNode()
        current_node = first_node
        while True:
            if list1 == None and list2 == None: # We reached the end of the both linked_lists
                break
            elif list1 == None:
                new_node = list2
                while new_node != None:
                    current_node.next = new_node
                    current_node = current_node.next
                    new_node = new_node.next
                break

            elif list2 == None:
                new_node = list1
                while new_node != None:
                    current_node.next = new_node
                    current_node = current_node.next
                    new_node = new_node.next
                break

            else:
                if list1.val <= list2.val:
                    print(list1.val)
                    current_node.next = list1
                    current_node = current_node.next
                    list1 = list1.next

                else:
                    print(list2.val)
                    current_node.next = list2
                    current_node = current_node.next
                    list2 = list2.next


        first_node = first_node.next
        return first_node
