#题目描述：
# 实现 int sqrt(int x) 函数。
# 计算并返回 x 的平方根，其中 x 是非负整数。
# 由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。
#
# 示例 1:
# 输入: 4
# 输出: 2
#
#
# 示例 2:
# 输入: 8
# 输出: 2
# 说明: 8 的平方根是 2.82842..., 由于返回类型是整数，小数部分将被舍去。
class Solution:
    #二分法查找
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        elif x == 1:
            return 1
        left = 1
        right = x//2
        while left < right:
            mid = (right+left+1)//2
            if mid**2 > x:
                right = mid-1
            else:
                left = mid
        return left
    #牛顿法


    def mySqrt2(self, x: int) -> int:
        if x == 0:
            return 0
        cur = 1
        while True:
            pre = cur
            cur = (cur+x/cur)/2
            if abs(cur-pre) < 1e-6:
                return int(cur)
if __name__ == "__main__":
    sl = Solution()
    x = 337910388
    print(sl.mySqrt(x))