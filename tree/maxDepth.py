# -- coding:utf-8 --
# 104 二叉树的最大深度
# 给定一个二叉树，找出其最大深度。二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。说明: 叶子节点是指没有子节点的节点。

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    #递归解决方法
    def maxDepth(self , root:TreeNode) -> int:

        if root == None:
            return 0
        else:
            left = self.maxDepth(root.left)
            right = self.maxDepth(root.right)
            return max(left , right) + 1

    #用桟来迭代
    #使用 DFS 策略访问每个结点，同时在每次访问时更新最大深度。
    def maxDepth2(self,root:TreeNode) -> int:
        stack = []
        if root is not None:
             stack.append((1,root))

        depth = 0
        while stack != []:
            current_depth , root = stack.pop()
            if root is not None:
                depth = max(depth,current_depth)
                stack.append((current_depth+1 , root.left))
                stack.append((current_depth+1 , root.right))
        return depth

    #BFS广度优先搜索
    def maxDepth3(self,root:TreeNode) -> int:
        if root is None:
            return 0
        queue = [(1,root)]
        depth = 0
        while queue:
            depth , node = queue.pop(0)
            if node.left:
                queue.append((depth+1 , node.left))
            if node.right:
                queue.append((depth+1 , node.right))
        return depth

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
print(solution.maxDepth3(root))