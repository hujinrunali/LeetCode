    #题目描述：
# 将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。
# 本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。
#
# 示例:
# 给定有序数组: [-10,-3,0,5,9],
# 一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：
#       0
#      / \
#    -3   9
#    /   /
#  -10  5

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums) -> TreeNode:
        if not nums:
            return None
        else:
            mid = (len(nums)-1)//2
            root = TreeNode(nums[mid])
            for i in range(len(nums)):
                if i != mid:
                    self.InsertNode(root,nums[i])
            return root

    def InsertNode(self,root,val):
        if val > root.val:
            if root.right:
                self.InsertNode(root.right,val)
            else:
                root.right = TreeNode(val)
        elif val <= root.val:
            if root.left:
                self.InsertNode(root.left,val)
            else:
                root.left = TreeNode(val)

    def sortedArrayToBST2(self, nums) -> TreeNode:

        # 先找到中间的数值
        datalen = len(nums)
        midlen = datalen // 2
        if datalen == 0:
            return None
        root = TreeNode(nums[midlen])
        root.left = self.sortedArrayToBST(nums[0:midlen])
        root.right = self.sortedArrayToBST(nums[midlen + 1:])
        return root

if __name__ == "__main__":
    nums = [0,1,2,3,4,5]
    sl  = Solution()
    sl.sortedArrayToBST(nums)
