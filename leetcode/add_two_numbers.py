# https://leetcode.com/problems/add-two-numbers/
# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        resp = []
        
        carry_over = 0
        
        it1 = l1
        it2 = l2
        
        while it1 or it2:
            val = carry_over
            if it1:
                val += it1.val
                it1 = it1.next
            if it2:
                val += it2.val
                it2 = it2.next
            # reset carry_over every step
            carry_over = val // 10
            val = val % 10
            
            resp.append(val)
        if carry_over:
            resp.append(carry_over)
            
        #print(resp)
        parent = None
        for num in reversed(resp):
            parent = ListNode(num, parent)
            
        return parent

