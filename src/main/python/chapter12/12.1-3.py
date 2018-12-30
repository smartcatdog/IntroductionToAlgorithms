"""
 二叉搜索树中序遍历非递归
 二叉搜索树：对于任意节点， 左孩子的数值比其根节点小， 右孩子数值比其根节点数值大
 leetcode:94  https://leetcode.com/problems/binary-tree-inorder-traversal/
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 递归解法，二叉搜索树任意一个节点依然为二叉搜索树，而中序遍历的定义为左根右
class Solution(object):

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)


# 递归循环可以相互转换，接下来为循环解法，参考算法导论第四版P162/12.1-3提示
# 用栈
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        res = []
        result = []
        cur = root
        if cur is None:
            return result
        while cur is not None or len(res) > 0:
            while cur is not None:
                res.append(cur)
                cur = cur.left
            cur = res.pop()
            result.append(cur.val)
            cur = cur.right
        return result

