# -- coding:utf-8 --
# 101 对称二叉树
# 给定一个二叉树，检查它是否是镜像对称的
# 可运用递归和迭代两种方法解决问题

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self,root:TreeNode) -> bool:

        return True



root = TreeNode(1)
node11 = TreeNode(2)
node12 = TreeNode(2)
node21 = TreeNode(3)
node22 = TreeNode(4)
node23 = TreeNode(4)
node24 = TreeNode(3)

root.left = node11
root.right = node12
node11.left = node21
node11.right = node22
node12.left = node23
node12.right = node24