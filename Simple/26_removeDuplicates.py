#题目描述：
#给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
#不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
# 示例 2:
#
# 给定 nums = [0,0,1,1,1,2,2,3,3,4],
#
# 函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。
#
# 你不需要考虑数组中超出新长度后面的元素。
#本程序只有放在力扣中才能测试
#解题思路：通过快慢指针i，j进行遍历，
#1.当nums[i]和nums[j]的值相同时，直接跳过
#2.当nums[i]和nums[j]的值不同时，i++,nums[i] = nums[j],其中原本i+1：j-1之间的值都是相同的
class Solution:
    def removeDuplicates(self, nums) -> int:
        if not nums:
            return 0
        i = 0
        for j in range(1,len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        return i+1
