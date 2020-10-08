#https://leetcode.com/explore/featured/card/october-leetcoding-challenge/559/week-1-october-1st-october-7th/3486/
'''
Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL

Example 2:

Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL


'''



# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def print_list(list_node):
    while list_node:
        print("%d->" % list_node.val)
        list_node = list_node.next
    print("NONE")

        
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not k:
            return head
        
        # get list length
        length = 0
        iter = head
        while iter:
            iter = iter.next
            length += 1
        
        mod_k = k % length
        if not mod_k:
            return head
        
        # get new head and tail:
        new_tail = head
        for i in range(0, length - mod_k - 1):
            new_tail = new_tail.next
        #print(new_tail.val)
        new_head = new_tail.next
        #print(new_head.val)
        new_tail.next = None
        # get attach the old tail to the list
        iter = new_head
        while iter.next:
            iter = iter.next
        iter.next = head

        return new_head
    
#s = Solution()
#ans = s.rotateRight(ListNode(0, ListNode(1, ListNode(2, None))), 4)
#print_list(ans)
