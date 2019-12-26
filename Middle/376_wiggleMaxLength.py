#题目描述：如果连续数字之间的差严格地在正数和负数之间交替，则数字序列称为摆动序列。第一个差（如果存在的话）可能是正数或负数。少于两个元素的序列也是摆动序列。
#例如， [1,7,4,9,2,5] 是一个摆动序列，因为差值 (6,-3,5,-7,3) 是正负交替出现的。相反, [1,4,7,2,5] 和 [1,7,4,5,5] 不是摆动序列，
# 第一个序列是因为它的前两个差值都是正数，第二个序列是因为它的最后一个差值为零。
#给定一个整数序列，返回作为摆动序列的最长子序列的长度。 通过从原始序列中删除一些（也可以不删除）元素来获得子序列，剩下的元素保持其原始顺序。
#实例：输入: [1,17,5,10,13,15,10,5,16,8]
#输出: 7
#解释: 这个序列包含几个长度为 7 摆动序列，其中一个可为[1,17,10,13,10,16,8]。
#方法一：暴力解法
class Solution:
    def wiggleMaxLength(self, nums) -> int:
        if nums.__len__() < 2:
            return nums.__len__()
        return 1+max(self.calculate(nums,0,True),self.calculate(nums,0,False))

    def calculate(self,nums,index,isUp):
        maxcount = 0
        for i in range(index+1,len(nums)):
            if (isUp and nums[i] > nums[index]) or (not isUp and nums[i] < nums[index]):
                maxcount = max(maxcount,1+self.calculate(nums,i,not isUp))

        return maxcount

#方法二：动态规划
class Solution2:
    def wiggleMaxLength(self, nums) -> int:
        datalen = len(nums)
        up = [0]*datalen
        down = [0]*datalen
        for i in range(1,datalen):
            for j in range(0,i):
                if nums[i] > nums[j]:
                    up[i] = max(up[i],down[j]+1)
                elif nums[i] < nums[j]:
                    down[i] = max(down[i],up[j]+1)
        return max(up[datalen-1],down[datalen-1])

#方法二：动态规划
class Solution3:
    def wiggleMaxLength(self, nums) -> int:
        datalen = len(nums)
        


if __name__ == "__main__":
    sl = Solution()
    nums = [1,17,5,10,13,15,10,5,16,8]

    print(sl.wiggleMaxLength(nums))