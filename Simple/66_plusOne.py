#题目描述：
# 给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
# 最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
# 你可以假设除了整数 0 之外，这个整数不会以零开头。
#
# 示例 1:
# 输入: [1,2,3]
# 输出: [1,2,4]
# 解释: 输入数组表示数字 123。
#
# 示例 2:
# 输入: [4,3,2,1]
# 输出: [4,3,2,2]
# 解释: 输入数组表示数字 4321。
#时间复杂度：最好的情况下O(n)
class Solution:
    def plusOne(self, digits) :
        datalen = len(digits)
        if datalen == 0:
            return []
        carry = 0
        i = datalen -1
        res = [0]*datalen
        while i >= 0:
            if i == datalen-1:
                res[i] = 1+digits[i]
            else:
                res[i] += digits[i] +carry
            if res[i] >= 10:
                res[i] = 0
                carry = 1
            else:
                carry = 0
            i -= 1
        if carry == 1:
            res.insert(0,1)
        return res