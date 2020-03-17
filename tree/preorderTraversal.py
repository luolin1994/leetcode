# 144 二叉树的前序遍历
#给定一个二叉树，返回它的前序遍历

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    # 递归解法
    def preorderTraversal(self,root:TreeNode) -> list:
        res = []
        def helper(root):
            if not root:
                return
            res.append(root.val)
            helper(root.left)
            helper(root.right)

        helper(root)
        return res

    # 迭代解法,深度优先搜索
    def preorderTraversal2(self,root:TreeNode) -> list:
        """
        res =[]
        p = root
        stack = []
        while p or stack:
            while p:
                res.append(p.val)
                stack.append(p)
                p = p.left
            p = stack.pop().right
        return res
        """

        if root is None:
            return []
        stack = [root]
        output = []
        while stack:
            root = stack.pop()
            if root is not None:
                output.append(root.val)
                if root.right is not None:
                    stack.append(root.right)
                if root.left is not None:    #桟的特性为后进先出
                    stack.append(root.left)
        return output




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
print(solution.preorderTraversal2(root))
