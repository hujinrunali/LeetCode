#题目描述：
# 罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。
# 字符          数值
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# 例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。
# 通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，
# 所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：
# 	I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
# 	X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。
# 	C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
#实例：
# 输入: "MCMXCIV"
# 输出: 1994
# 解释: M = 1000, CM = 900, XC = 90, IV = 4.
#代码时间复杂度分析：O(n)
class Solution:
    def romanToInt(self, s: str) -> int:
        slen = len(s)
        if slen == 0:
            return 0
        mydic = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        res = 0
        for i in range(slen-1):
            if mydic[s[i]]>=mydic[s[i+1]]:
                res += mydic[s[i]]
            else:
                res -= mydic[s[i]]
        res += mydic[s[slen-1]]
        return res


if __name__ == "__main__":
    sl = Solution()
    print(sl.romanToInt("MCMXCIV"))