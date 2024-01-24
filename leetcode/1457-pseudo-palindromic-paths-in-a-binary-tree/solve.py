# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        def countPalindromes(node: TreeNode, prev):
            nextPrev = prev.copy()
            if (node.val in prev):
                nextPrev.remove(node.val)
            else:
                nextPrev.add(node.val)
            if (node.left is None and node.right is None):
                counter = collections.Counter(nextPrev)
                odd_count = 0
                for value in counter.values():
                    if value % 2 == 1:
                        odd_count += 1
                if (odd_count > 1):
                    return 0
                else:
                    return 1
            return (0 if node.left is None else countPalindromes(node.left, nextPrev))\
            + (0 if node.right is None else countPalindromes(node.right, nextPrev))
        return countPalindromes(root, set())
