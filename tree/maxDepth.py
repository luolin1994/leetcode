# 104 二叉树的最大深度
# 给定一个二叉树，找出其最大深度。二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。说明: 叶子节点是指没有子节点的节点。

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self , root:TreeNode) -> int:

        if root == None:
            return 0
        else:
            left = self.maxDepth(root.left)
            right = self.maxDepth(root.right)
            return max(left , right) + 1

root = TreeNode(3)
node11 = TreeNode(9)
node12 = TreeNode(20)
node21 = TreeNode(15)
node22 = TreeNode(7)



root.left = node11
root.right = node12
node12.left = node21
node12.right = node22

solution = Solution()
print(solution.maxDepth(root))