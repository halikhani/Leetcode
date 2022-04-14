# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Input: l1 = [0], l2 = [0]
# Output: [0]

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

# ================================================================================================

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def calc_num(listnode):
            current = listnode
            val = 0
            pow = 1
            while True:
                val += (current.val*pow)
                if current.next == None:
                    break
                else:
                    current = current.next
                    pow *= 10
            return val
                
        def get_linkedlist(number):
            
            new = ListNode()
            firstnode = new
            while True:
                res = number % 10
                new.val = res
                number = number // 10
                if number == 0:
                    break
                else:
                    new.next = ListNode()
                    new = new.next
            return firstnode
        
        
        num1 = calc_num(l1)
        num2 = calc_num(l2)
        
        result = num1 + num2
        return get_linkedlist(result)
        