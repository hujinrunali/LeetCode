#题目描述：判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
#实例：示例 1:
#输入: 121
#输出: true
#算法的时间复杂度分析：因为输入x的位数有限，所以时间复杂度为O(1)
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x < 0) or (x%10 == 0 and x != 0):
            return False
        reversenum = 0
        while x > reversenum:
            reversenum = reversenum*10 + x%10
            x //= 10
        return x == reversenum or x == reversenum//10

if __name__ == '__main__':
    sl = Solution()
    print(sl.isPalindrome(11))