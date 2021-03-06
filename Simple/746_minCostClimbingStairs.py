#题目描述：
# 数组的每个索引做为一个阶梯，第 i个阶梯对应着一个非负数的体力花费值 cost[i](索引从0开始)。
# 每当你爬上一个阶梯你都要花费对应的体力花费值，然后你可以选择继续爬一个阶梯或者爬两个阶梯。
# 您需要找到达到楼层顶部的最低花费。在开始时，你可以选择从索引为 0 或 1 的元素作为初始阶梯。
#
# 示例 1:
# 输入: cost = [10, 15, 20]
# 输出: 15
# 解释: 最低花费是从cost[1]开始，然后走两步即可到阶梯顶，一共花费15。
#
# 示例 2:
# 输入: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
# 输出: 6
# 解释: 最低花费方式是从cost[0]开始，逐个经过那些1，跳过cost[3]，一共花费6。
class Solution:
    def minCostClimbingStairs(self, cost) -> int:
        datalen = len(cost)
        if datalen == 0:
            return 0
        elif datalen == 1:
            return cost[0]
        elif datalen == 2:
            return min(cost)
        distance = [0] * datalen
        distance[0] = cost[0]
        distance[1] = cost[1]
        for i in range(2, datalen):
            distance[i] = min(distance[i - 1], distance[i - 2]) + cost[i]
        return min(distance[-1], distance[-2])
    #可以将上楼梯的过程想成下楼梯
    def minCostClimbingStairs2(self, cost):
        f1 = f2 = 0
        for x in reversed(cost):
            f1,f2 = x+min(f1,f2),f1
        return min(f1,f2)
