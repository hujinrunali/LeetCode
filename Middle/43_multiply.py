#题目描述：
# 给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。
#
# 示例 1
# 输入: num1 = "2", num2 = "3"
# 输出: "6"
#
# 示例 2:
# 输入: num1 = "123", num2 = "456"
# 输出: "56088"
#
# 说明：
# num1 和 num2 的长度小于110。
# num1 和 num2 只包含数字 0-9。
# num1 和 num2 均不以零开头，除非是数字 0 本身。
# 不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '' or num2 == '':
            return ''
        if num1 == '0' or num2 == '0':
            return '0'
        datalen1 = len(num1)
        datalen2 = len(num2)
        datalen = min(datalen1, datalen2)
        numlen = ''
        numshort = ''
        if datalen1 > datalen2:
            numlen = num1
            numshort = num2
        else:
            numlen = num2
            numshort = num1
        i = -1
        count = 0
        res = ''
        prestr = '0'
        while (i >= -datalen):
            tmpres = self.subMultiply(numlen,numshort[i])
            for _ in range(count):
                tmpres += '0'
            res = self.Add(tmpres, prestr)
            prestr = res
            i -=1
            count += 1
        return res

    def subMultiply(self, nums, num):
        if nums == '' or num == '':
            return 0
        datalen = len(nums)
        numint = int(num)
        i = -1
        res = ''
        carry = 0
        while i >= -datalen:
            tmpint = int(nums[i]) * numint + carry
            if tmpint // 10 != 0:
                carry = tmpint // 10
                tmpint = tmpint % 10
            else:
                carry = 0
            res = str(tmpint) + res
            i -= 1
        if carry != 0:
            res = str(carry) + res
        return res

    def Add(self, num1, num2):
        if num1 == '':
            return num2
        if num2 == '':
            return num1
        datalen1 = len(num1)
        datalen2 = len(num2)
        if datalen1 < datalen2:
            num1,num2 = num2,num1
            datalen1,datalen2 = datalen2,datalen1
        res = ''
        carry = 0
        i = -1
        while i >= -datalen2:
            tmpint = int(num1[i]) + int(num2[i]) + carry
            if tmpint >= 10:
                carry = 1
                tmpint = tmpint - 10
            else:
                carry = 0
            res = str(tmpint) + res
            i -= 1
        if datalen1 > datalen2:
            while i >= -datalen1:
                tmpint = int(num1[i]) + carry
                if tmpint >= 10:
                    carry = 1
                    tmpint = tmpint - 10
                else:
                    carry = 0
                res = str(tmpint) + res
                i -= 1
        if carry != 0:
            res = str(carry) + res
        return res

#优化算法
class Solution2:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0':
            return '0'
        if num2 == '0':
            return '0'
        l1 = len(num1)
        l2 = len(num2)
        if l1 < l2:
            num1,num2 = num2,num1
            l1,l2 = l2,l1
        res = [0]*(l1+l2)
        for i in range(l2-1,-1,-1):
            n1 = int(num2[i])
            for j in range(l1-1,-1,-1):
                n2 = int(num1[j])
                tmpsum = res[i+j+1]+n1*n2
                res[i+j+1] = tmpsum%10
                res[i+j] += tmpsum//10
        if res[0] == 0:
            res.remove(0)
        return ''.join([str(x) for x in res])

if __name__ == "__main__":
    sl = Solution2()
    a = '123'
    b = '456'
    print(sl.multiply(a,b))