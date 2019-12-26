#题目描述：
# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
#
# 示例:
#
# 输入: [-2,1,-3,4,-1,2,1,-5,4],
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
#时间复杂度：O(n)
import math
class Solution:
    def maxSubArray2(self, nums) -> int:
        datalen = len(nums)
        if datalen == 0:
            return 0
        elif datalen == 1:
            return nums[0]
        mysum = 0
        mymax = -1000000000
        for subn in nums:
            if mysum + subn > subn:
                mysum = mysum + subn
            else:
                mysum = subn
            if mysum > mymax:
                mymax = mysum
        return mymax

    #采用分治法的求解
    #时间复杂度为O(nlgn)
    def maxSubArray(self, nums) -> int:
        datalen = len(nums)
        if datalen == 0:
            return 0
        if datalen == 1:
            return nums[0]
        mid = datalen // 2
        left_max = self.maxSubArray(nums[0:mid])
        right_max = self.maxSubArray(nums[mid:])
        mid_max = self.maxSubArraymid(nums, mid)
        return max(left_max, right_max, mid_max)

    def maxSubArraymid(self, nums, mid):
        left_max = float('-inf')
        right_max = float('-inf')
        sum = 0
        for i in range(mid, -1, -1):
            sum += nums[i]
            if sum > left_max:
                left_max = sum
        sum = 0
        for i in range(mid + 1, len(nums)):
            sum += nums[i]
            if sum > right_max:
                right_max = sum
        return max(left_max, right_max, left_max + right_max)

if __name__ == "__main__":
    sl = Solution()
    a = [1,2,-1]
    print(sl.maxSubArray(a))