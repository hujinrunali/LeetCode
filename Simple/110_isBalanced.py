#题目描述：leetcode110
# 给定一个二叉树，判断它是否是高度平衡的二叉树。
# 本题中，一棵高度平衡二叉树定义为：
# 一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。
#
# 示例 1:
# 给定二叉树 [3,9,20,null,null,15,7]
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回 true 。
#
# 示例 2:
# 给定二叉树 [1,2,2,3,3,null,null,4,4]
#        1
#       / \
#      2   2
#     / \
#    3   3
#   / \
#  4   4
# 返回 false 。
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # 遍历树的全部节点
        #时间复杂度较大
        dumplist = []
        if not root:
            return True
        dumplist.append(root)
        while dumplist:
            tempNode = dumplist.pop(0)
            if (abs(self.BinaryTreeDeepth(tempNode.left) - self.BinaryTreeDeepth(tempNode.right)) > 1):
                return False
            if tempNode.left:
                dumplist.append(tempNode.left)
            if tempNode.right:
                dumplist.append(tempNode.right)
        return True


        # 定义求解二叉树深度的函数
    def BinaryTreeDeepth(self, root):
        if not root:
            return 0
        leftdeepth = self.BinaryTreeDeepth(root.left)
        rightdeepth = self.BinaryTreeDeepth(root.right)
        return max(leftdeepth, rightdeepth) + 1



#别人写的代码
#思路：如果遇到不平衡的子树则从中间截断返回
class Solution2:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.depth(root) != -1

    def depth(self, root):
        if not root: return 0
        left = self.depth(root.left)
        if left == -1: return -1
        right = self.depth(root.right)
        if right == -1: return -1
        return max(left, right) + 1 if abs(left - right) < 2 else -1
