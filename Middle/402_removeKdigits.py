#题目描述：给定一个以字符串表示的非负整数 num，移除这个数中的 k 位数字，使得剩下的数字最小。
#实例：输入: num = "1432219", k = 3
#输出: "1219"
#解释: 移除掉三个数字 4, 3, 和 2 形成一个新的最小的数字 1219。
#解法一：
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        numlist = list(num)
        datalen = len(numlist)
        recount = 0
        if k == 0 :
            return num
        if k >= datalen:
            return '0'
        for i in range(k):
            datalen = len(numlist)
            for j in range(1,datalen):
                if numlist[j] < numlist[j-1]:
                    numlist.remove(numlist[j-1])
                    recount += 1
                    break
        for i in range(k-recount):
            numlist.pop()
        result = ''.join(numlist).lstrip('0')
        if result == '':
            result = '0'
        return result
