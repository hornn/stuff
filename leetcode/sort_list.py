# https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/560/week-2-october-8th-october-14th/3493/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def bubbleSort(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        iter_i = head
        while iter_i:
            if iter_i.next:
                # improvement 1 - if value equals to previous val, skip
                iter_j = iter_i.next
                if iter_j.val != iter_i.val:
                    while iter_j:
                        if iter_i.val > iter_j.val:
                            big_val = iter_i.val
                            iter_i.val = iter_j.val
                            iter_j.val = big_val
                        iter_j = iter_j.next
            iter_i = iter_i.next
        return head    
    
    
    def countSort(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # count will be from -10^5 to 10^5
        count_dict = dict()
        
        # first iteration to count number of each number
        iter = head
        length = 0
        while iter:
            val = iter.val 
            count_dict[val] = count_dict.get(val, 0) + 1
            iter = iter.next
            length += 1
            
        # at this point we have the count of each number, as well as the total size.
        # iterate over the full range, and for each count create add this many nodes to the list.
        res = None
        for i in range(pow(10,5), pow(-10, 5) -1, -1):
            count = count_dict.get(i)
            if count:
                for _ in range(0, count):
                    res = ListNode(i, res)
        return res            
        
        '''
        # update count to have the number of values before it
        total = count_dict.get(pow(-10, 5), 0)
        for i in range(pow(-10,5) + 1, pow(10^5) + 1):
            count = count_dict.get(i)
            if count:
                count_dict[i] = count + total
                total += count
            #count_dict[i] = count_dict.get(i, 0) + count_dict.get(i-1, 0)
            
        # create a result array with the length of input list
        res_arr = [None] * length
        
        
            #B[C[A[i]]]=A[i]}
  #C [ A [ i ] ] = C [ A [ i ] ] − 1 {\displaystyle \ C[A[i]]=C[A[i]]-1} {\displaystyle \ C[A[i]]=C[A[i]]-1}
        '''
        
    
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """ 
        
        return self.countSort(head)
