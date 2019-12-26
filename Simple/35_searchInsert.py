#题目描述：
# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
# 你可以假设数组中无重复元素。
# 示例 1:
# 输入: [1,3,5,6], 5
# 输出: 2
# 示例 2:
# 输入: [1,3,5,6], 2
# 输出: 1
#时间复杂度：遍历数组O(n)
class Solution:
    def searchInsert(self, nums, target: int) -> int:
        datalen = len(nums)
        if datalen == 0:
            return 0
        res = 0
        i = 0
        while i < datalen:
            if nums[i] >= target:
                res = i
                break
            i += 1
        if i == datalen:
            res = datalen
        return res

    #Python一行代码写法
    def searchInsert2(self, nums, target: int):
        return len([i for i in nums if i < target])