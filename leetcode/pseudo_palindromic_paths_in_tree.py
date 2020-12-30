# https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def is_palindrome(self, nums: list) -> bool:
        # if length is even, all occurrences must be even
        # if length is odd, exactly one occurence must be odd, the rest even
        is_len_even = len(nums) % 2 == 0
        odd_count = 0
        
        for i in range(10):
            is_even_freq = nums.count(i) % 2 == 0
            if not is_even_freq:
                if is_len_even or odd_count == 1:
                    return False
                odd_count += 1
        if is_len_even:
            return odd_count == 0
        else:
            return odd_count == 1
        
    
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        palindromes = 0
        
        stack = deque()
        stack.append((root, []))
        while stack:
            node, parents = stack.pop()
            if node.left:
                stack.append((node.left, parents + [node.val]))
            if node.right:
                stack.append((node.right, parents + [node.val]))
            if not node.left and not node.right:
                if self.is_palindrome(parents + [node.val]):
                    palindromes += 1
        return palindromes
