#题目描述：
# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
# 注意：给定 n 是一个正整数。
#
# 示例 1：
# 输入： 2
# 输出： 2
# 解释： 有两种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶
# 2.  2 阶
#
# 示例 2：
# 输入： 3
# 输出： 3
# 解释： 有三种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶 + 1 阶
# 2.  1 阶 + 2 阶
# 3.  2 阶 + 1 阶
#题目解析：n级台阶的到达方式有两种，n-1级台阶走一步，或者n-2级台阶走两步
#f(n) = f(n-1)+f(n-2)
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        if n < 3:
            return n
        pre1 = 1
        pre2 = 2
        pre3 = 0
        for _ in range(3,n+1):
            pre3 = pre1+pre2
            pre1 = pre2
            pre2 = pre3
        return pre3
