#题目描述：
# 给定一个数组 nums 和一个值 val，你需要原地移除所有数值等于 val 的元素，返回移除后数组的新长度。
# 不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
# 元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
#
# 示例 1:
# 给定 nums = [3,2,2,3], val = 3,
# 函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。
# 你不需要考虑数组中超出新长度后面的元素。
class Solution:
    def removeElement(self, nums, val: int) -> int:
        if not nums:
            return 0
        datalen = len(nums)
        i = 0
        while i < datalen and nums[i] == val:
            i += 1
        if i == datalen:
            return 0
        else:
            nums[0] = nums[i]
        tempi = 1
        for j in range(i+1,datalen):
            if nums[j] != val:
                nums[tempi] = nums[j]
                tempi += 1
        return tempi
