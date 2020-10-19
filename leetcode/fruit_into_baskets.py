# https://leetcode.com/problems/fruit-into-baskets/
class Solution(object):
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        
        # structure for keeping data of each tree:
        # 1. length starting from this tree
        # 2. set of numbers of the sequence (can be 1 or 2 nums)
        # 3. length of sequence of the same fruit.
        # example
        # for [1,2,3,2,2,1]
        # 5: (1, (1), 1)  
        # 4: (2 ,(1,2), 1) - there is only 1 fruit of 2 value
        # 3: (3, (1,2), 2) - there are 2 fruits of 2 values 
        # 2: (3, (2,3), 1) - there is only 1 fruit of 3 values, 
        #                    but we used the data from the previous tree to determine the current sequence (1 + 2)
        # 1: (4, (2,3), 1)
        # 0: (2, (1,2), 1)
        
        # print(tree)
        data = dict()
        max_seq = 0
        for idx in range(len(tree) - 1, -1, -1):
            prev = data.get(idx+1)
            if not prev:
                # print(tree[idx])
                data[idx] = (1, set([tree[idx]]), 1)
                max_seq = 1
            else:
                prev_max, prev_nums, prev_sames = prev
                prev_val = tree[idx+1]
                new_val = tree[idx]
                if new_val == prev_val:
                    # increase the sames sequence
                    data[idx] = (prev_max + 1, prev_nums, prev_sames + 1)
                elif new_val in prev_nums:
                    # new sames sequence
                    data[idx] = (prev_max + 1, prev_nums, 1)
                else:
                    # new everything
                    data[idx] = (1 + prev_sames, set([new_val, prev_val]), 1)
                max_seq = max(max_seq, data[idx][0])
        # print(data)
        return max_seq
                    
                
        
