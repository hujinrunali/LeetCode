#题目说明：leetcode107题
# 给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）
# 例如：
# 给定二叉树 [3,9,20,null,null,15,7],
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
# 返回其自底向上的层次遍历为：
# [
#   [15,7],
#   [9,20],
#   [3]
# ]

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.list = []

    def levelOrderBottom(self, root: TreeNode):
        if not root:
            return []
        queue = [root]
        while queue:
            tmplist = []
            queuelen = len(queue)
            for _ in range(queuelen):
                tmproot = queue.pop(0)
                tmplist.append(tmproot.val)
                if tmproot.left:
                    queue.append(tmproot.left)
                if tmproot.right:
                    queue.append(tmproot.right)
            self.list.append(tmplist)
        return reversed(self.list)

    #别人写的思路比较好的代码
    #递归的方式
    def levelOrderBottom2(self, root: TreeNode):
        res = []
        def helper(root, depth):
            if not root: return
            if depth == len(res):
                res.insert(0, [])
            res[-(depth + 1)].append(root.val)
            helper(root.left, depth + 1)
            helper(root.right, depth + 1)
        helper(root, 0)
        return res


if __name__ == "__main__":
    root = TreeNode(3)
    leaf1 = TreeNode(9)
    leaf2 = TreeNode(20)
    leaf3 = TreeNode(15)
    leaf4 = TreeNode(7)
    root.left = leaf1
    root.right = leaf2
    leaf2.left = leaf3
    leaf2.right = leaf4
    sl = Solution()
    sl.levelOrderBottom(root)