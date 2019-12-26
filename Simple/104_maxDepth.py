#题目描述：
# 给定一个二叉树，找出其最大深度。
# 二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
# 说明: 叶子节点是指没有子节点的节点。
#
# 示例：
# 给定二叉树 [3,9,20,null,null,15,7]，
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回它的最大深度 3 。
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    #递归做法：时间复杂度为O(n),
    #空间复杂度：最好O(NlgN),最坏O(N)
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        leftdepth = self.maxDepth(root.left)
        rightdepth = self.maxDepth(root.right)
        return max(leftdepth,rightdepth)+1

    # 非递归做法：时间复杂度为O(n),
    # 空间复杂度：O(N)
    def maxDepth2(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = [(root,1)]
        maxdepth = 0
        while queue:
            tmproot,tmpdepth = queue.pop(0)
            if tmpdepth > maxdepth:
                maxdepth = tmpdepth
            if tmproot.left:
                queue.append((tmproot.left,tmpdepth+1))
            if tmproot.right:
                queue.append((tmproot.right,tmpdepth+1))
        return maxdepth

