#题目描述：
# 给定两个二叉树，编写一个函数来检验它们是否相同。
# 如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。
#
# 示例 1:
# 输入:       1         1
#           / \       / \
#          2   3     2   3
#
#         [1,2,3],   [1,2,3]
# 输出: true
#
# 示例 2:
# 输入:      1          1
#           /           \
#          2             2
#
#         [1,2],     [1,null,2]
# 输出: false
#
# 示例 3:
# 输入:       1         1
#           / \       / \
#          2   1     1   2
#
#         [1,2,1],   [1,1,2]
# 输出: false
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    #递归的方式实现，时间复杂度为O(N),
    # 平均空间复杂度为O(lgN)，最坏的空间复杂度为O(N),主要的空间用来维护调用栈
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p == None and q == None:
            return True
        elif p != None and q != None and p.val == q.val:
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        else:
            return False

    #非递归层次遍历的方式实现,时间复杂度为O(N),
    # 平均空间复杂度为O(lgN)，最坏的空间复杂度为O(N),主要的空间用来维护队列
    def isSameTree2(self, p: TreeNode, q: TreeNode) -> bool:
        queue = [(p, q)]
        while queue:
            tmpp, tmpq = queue.pop(0)
            flag = self.checkTrees(tmpp, tmpq)
            if not flag:
                return False
            if tmpp and tmpq:
                queue.append((tmpp.left, tmpq.left))
                queue.append((tmpp.right, tmpq.right))
        return True

    def checkTrees(self, p: TreeNode, q: TreeNode):
        if p == None and q == None:
            return True
        elif p != None and q != None and p.val == q.val:
            return True
        else:
            return False