# https://leetcode.com/problems/linked-list-random-node/
from random import randrange

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    len = 0
    head = None
    
    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head
        while head:
            self.len += 1
            head = head.next

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        idx = randrange(self.len)
        res = self.head
        # iterate for idx-1 more steps - index 0 is head
        for _ in range(idx):
            res = res.next
        return res.val
    

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
