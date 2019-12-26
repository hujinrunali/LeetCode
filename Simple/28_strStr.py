# #题目描述：
# 实现 strStr() 函数。
#
# 给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。
# 如果不存在，则返回  -1。
#
# 示例 1:
# 输入: haystack = "hello", needle = "ll"
# 输出: 2
#字符串匹配算法
#算法的时间复杂度分析：
#最坏的情况：O(m*n) m-待匹配串的长度 n-匹配串的长度
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        j = 0
        hLen= len(haystack)
        nLen = len(needle)
        if nLen == 0:
            return 0
        next = self.GetNext(needle)
        while i < hLen and j < nLen:
            if(j == -1 or haystack[i] == needle[j]):
                i += 1
                j += 1
            else:
                j = next[j]
        if j == nLen:
            return i-j
        else:
            return -1

    def GetNext(self,needle):
        pLen = len(needle)
        next = [0]*pLen
        next[0] = -1
        k = -1
        j = 0
        while j < pLen-1:
            if k == -1 or needle[k] == needle[j]:
                k += 1
                j += 1
                next[j] = k
            else:
                k = next[k]
        return next

if __name__ == "__main__":
    haystack = "aaaaa"
    needle = "bba"
    sl = Solution()
    a = sl.strStr(haystack,needle)
    print(a)