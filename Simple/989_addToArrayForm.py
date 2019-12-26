#题目描述：
# 对于非负整数X而言，X的数组形式是每位数字按从左到右的顺序形成的数组。例如，如果
# X = 1231，那么其数组形式为[1, 2, 3, 1]。
#
# 给定非负整数X的数组形式A，返回整数X + K的数组形式。
#
# 示例
# 输入：A = [1, 2, 0, 0], K = 34
# 输出：[1, 2, 3, 4]
# 解释：1200 + 34 = 1234
#
# 解释
# 输入：A = [2, 7, 4], K = 181
# 输出：[4, 5, 5]
# 解释：274 + 181 = 455
class Solution:
    def addToArrayForm(self, A, K):
        if K == 0:
            return A
        if not A:
            return []
        datalen = len(A)
        i,carry = datalen-1,0
        res = []
        res.append((A[i]+K)%10)
        carry = (A[i]+K)//10
        i -= 1
        while i >= 0 or carry >0:
            if i >= 0:
                carry = carry+A[i]
                i -= 1
            res.append(carry%10)
            carry = carry//10
        return res[::-1]