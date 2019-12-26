#题目描述
# 报数序列是一个整数序列，按照其中的整数的顺序进行报数，得到下一个数。其前五项如下：
# 1.1
# 2.11
# 3.21
# 4.1211
# 5.111221
#
# 1被读作"one 1"("一个一"), 即11。
# 11被读作"two 1s"("两个一"）, 即21。
# 21被读作"one 2", "one 1" （"一个二", "一个一"), 即1211。
#
# 给定一个正整数
# n（1 ≤ n ≤ 30），输出报数序列的第n项。
#
# 注意：整数顺序将表示为一个字符串。
#
# 示例
# 1:
#
# 输入: 1
# 输出: "1"
#
# 示例
# 2:
#
# 输入: 4
# 输出: "1211"
class Solution:
    def countAndSay(self, n: int) -> str:
        res = '1'
        for _ in range(n - 1):
            res = self.getResult(res)
        return res

    def getResult(self, nstr) -> str:
        datalen = len(nstr)
        if datalen == 1:
            return '11'
        count = 1
        pre = nstr[0]
        res = ''
        for i in range(1, datalen):
            if pre == nstr[i]:
                count += 1
            else:
                res += str(count) + pre
                pre = nstr[i]
                count = 1
        res += str(count) + pre
        return res

if __name__ == "__main__":
    sl = Solution()
    print(sl.countAndSay(4))