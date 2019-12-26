#题目描述：
# 给定一个二叉树，检查它是否是镜像对称的。
# 例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
#
# 但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
#     1
#    / \
#   2   2
#    \   \
#    3    3
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        else:
            return self.helper(root.left, root.right)

    def helper(self, left, right):
        if left == None and right == None:
            return True
        elif left != None and right != None and left.val == right.val:
            return self.helper(left.left, right.right) and self.helper(left.right, right.left)
        else:
            return False

    #非递归的方式实现
    #先加入两个root,然后将节点的左右子节点按照相反的顺序加入队列
    def isSymmetric2(self, root: TreeNode) -> bool:
        queue = [root,root]
        while queue:
            tmp1 = queue.pop(0)
            tmp2 = queue.pop(0)
            if tmp1 == None and tmp2 == None:
                continue
            elif tmp1 == None or tmp2 == None:
                return False
            elif tmp1.val != tmp2.val:
                return False
            queue.append(tmp1.left)
            queue.append(tmp2.right)
            queue.append(tmp1.right)
            queue.append(tmp2.left)
        return True