#题目描述：编写一个函数来查找字符串数组中的最长公共前缀。
# 如果不存在公共前缀，返回空字符串 ""。
# 示例 1:
# 输入: ["flower","flow","flight"]
# 输出: "fl"
#方法一：分治算法
#递归的思想：将问题进行逐一拆分，然后求解

class Solution:
    #假设字符列表为：m*n-n个字符串，每个字符串有m个字符
    # 算法时间复杂度分析：O(m*n)
    def longestCommonPrefix(self, strs) -> str:
        #strs中没有元素或者只有一个元素之间返回
        if len(strs) <= 0:
            return ""
        if len(strs) <= 1:
            return strs[0]

        #strs中有超过一个元素时,进行递归操作
        reststr = self.longestCommonPrefix(strs[1:])
        return self.getCommonPart(strs[0], reststr)

    #算法的时间复杂度分析：O(m*lg(n))
    def longestCommonPrefix2(self,strs):
       #进行二分的分治策略
       #特殊情况的判定
        if len(strs) <= 0:
            return ""
        if len(strs) <= 1:
            return strs[0]
        return self.longestCommonPrefixDiv(strs,0,len(strs)-1)

    def longestCommonPrefixDiv(self,strs,start,end):
        if start >= end:
            return strs[start]
        mid = (start+end)//2
        str1 = self.longestCommonPrefixDiv(strs,start,mid)
        str2 = self.longestCommonPrefixDiv(strs,mid+1,end)
        return self.getCommonPart(str1,str2)

    def getCommonPart(self,str1,str2):
        if str1 == "" or str2 == "":
            return ''
        tmplen = min(len(str1), len(str2))
        result = ''
        for i in range(tmplen):
            if str1[i] == str2[i]:
                result += str1[i]
            else:
                break
        return result
#方法二：二分查找法
class Solution2:
    def longestCommonPrefix(self, strs) -> str:
        pass

#方法三：通过字典树的方式查找
class Solution3:
    def longestCommonPrefix(self, strs) -> str:
        pass

