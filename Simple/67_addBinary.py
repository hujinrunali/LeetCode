# 给定两个二进制字符串，返回他们的和（用二进制表示）。
# 输入为非空字符串且只包含数字 1 和 0。
# 示例 1:
# 输入: a = "11", b = "1"
# 输出: "100"
#
# 示例 2:
# 输入: a = "1010", b = "1011"
# 输出: "10101"
#算法时间复杂度分析：O(max(m,n)),m,n为a,b所含元素的个数
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        l1 = len(a)
        l2 = len(b)
        if l1 == 0:
            return b
        if l2 == 0:
            return a
        if l1 < l2:
            a,b = b,a
            l1,l2 = l2,l1
        carry = 0
        i = -1
        res = ''
        while i >= -l2:
            tmpint = int(a[i])+int(b[i]) + carry
            if tmpint in [0,1]:
                carry = 0
            elif tmpint == 2:
                carry = 1
                tmpint = 0
            elif tmpint == 3:
                carry = 1
                tmpint = 1
            res = str(tmpint)+res
            i -= 1
        while i >= -l1:
            tmpint = int(a[i]) + carry
            if tmpint in [0,1]:
                carry = 0
            elif tmpint == 2:
                carry = 1
                tmpint = 0
            elif tmpint == 3:
                carry = 1
                tmpint = 1
            res = str(tmpint)+res
            i -= 1
        if carry == 1:
            res = str(carry)+res
        return res

    #比较简便的做法
    def addBinary2(self, a: str, b: str) -> str:
        res,carry = '',0
        i = len(a)-1
        j = len(b)-1
        while i>=0 or j >= 0:
            if i>=0:
                carry += ord(a[i])-ord('0')
            if j >= 0:
                carry += ord(b[j]) - ord('0')
            res += str(carry%2)
            carry = carry//2
            i,j = i-1,j-1
        if carry != 0:
            res += str(carry)
        return res[::-1]

if __name__ == "__main__":
    sl = Solution()
    a = '11'
    b = '1'
    print(sl.addBinary2(a,b))