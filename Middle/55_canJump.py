#题目描述：给定一个非负整数数组，你最初位于数组的第一个位置。
#数组中的每个元素代表你在该位置可以跳跃的最大长度。
#判断你是否能够到达最后一个位置。
#输入: [2,3,1,1,4]
#输出: true
#解释: 从位置 0 到 1 跳 1 步, 然后跳 3 步到达最后一个位置。

class Solution:
    ##################################
    def __init__(self):
        self.memo = []

    #方法一：回溯算法
    def canJump(self, nums) -> bool:
        return self.canJumpFromPosition(0, nums)

    def canJumpFromPosition(self, position, nums):
        if (position == len(nums) - 1):
            return True

        furthestJump = min(position + nums[position], len(nums) - 1)
        for i in range(position + 1, furthestJump + 1):
            if (self.canJumpFromPosition(i, nums)):
                return True
        return False
    #####################################

    #方法二：自顶向下的动态规划
    #0-UNKNOW 1-Bad 2-Good
class Solution2:
    def __init__(self):
        self.memo = []

    def canJump2(self, nums) -> bool:
        for i in range(len(nums)-1):
            self.memo.append(0)
        self.memo.append(2)
        return self.canJumpFromPosition2(0,nums)

    def canJumpFromPosition2(self, position, nums):
        if(self.memo[position] != 0):
            return True if self.memo[position] == 2 else False

        furthestJump = min(position+nums[position],len(nums)-1)
        for i in range(position+1,furthestJump+1):
            if(self.canJumpFromPosition2(i,nums)):
                self.memo[position] = 2
                return True
        self.memo[position] = 1
        return False

    #方法三：自底向上的动态规划
    # 0-UNKNOW 1-Bad 2-Good
class Solution3:
    def __init__(self):
        self.memo = []

    def canJump(self, nums) -> bool:
        for i in range(len(nums)-1):
            self.memo.append(0)
        self.memo.append(2)
        for i in range(len(nums)-2,-1,-1):
            furthestJump = min(i+nums[i],len(nums)-1)
            for j in range(i+1,furthestJump+1):
                if(self.memo[j] == 2):
                    self.memo[i] = 2
        return self.memo[0] == 2

        #方法三：贪心算法
class Solution4:
    def canJump(self, nums) -> bool:
        lastgoodpos = len(nums)-1
        for i in range(len(nums)-2,-1,-1):
            if(i+nums[i] >= lastgoodpos):
                lastgoodpos = i
        return lastgoodpos == 0
