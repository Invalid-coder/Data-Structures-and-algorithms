"""
Given the root of a binary tree, return the
inorder traversal of its nodes' values.

Example 1:


Input: root = [1,null,2,3]
Output: [1,3,2]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root):
        arr = []
        self.helper(root, arr)
        return arr

    def helper(self, root, arr):
        if root:
            if root.left:
                self.helper(root.left, arr)
            arr.append(root.val)
            if root.right:
                self.helper(root.right, arr)

    def inorderTraversal_iterative(self, root):
        arr = []
        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            arr.append(curr.val)
            curr = curr.right
        return arr


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    n1 = TreeNode(2)
    n2 = TreeNode(3)
    root.right = n1
    n1.left = n2
    print(s.inorderTraversal_iterative(root))