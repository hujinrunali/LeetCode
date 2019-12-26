#题目描述：
# 给定一个按非递减顺序排序的整数数组A，返回每个数字的平方组成的新数组，要求也按非递减顺序排序。
#
# 示例
# 1：
# 输入：[-4, -1, 0, 3, 10]
# 输出：[0, 1, 9, 16, 100]
#
# 示例
# 2：
# 输入：[-7, -3, 2, 3, 11]
# 输出：[4, 9, 9, 49, 121]
#算法的时间复杂度为：O(n)
class Solution:
    def sortedSquares(self, A):
        datalen = len(A)
        if datalen == 0:
            return []
        res = []
        if A[0] < 0 and A[-1] >= 0:
            #找到中间的数
            i = 0
            j = 0
            for k in range(datalen-1):
                if A[k] < 0 and A[k+1] >= 0:
                    i = k
                    j = k+1
                    break
            while i >= 0 and j <= datalen -1:
                if A[i]**2 < A[j]**2:
                    res.append(A[i]**2)
                    i -= 1
                else:
                    res.append(A[j]**2)
                    j +=1
            while i >= 0:
                res.append(A[i]**2)
                i -= 1
            while j <= datalen -1:
                res.append(A[j]**2)
                j += 1
        else:
            for num in A:
                res.append(num**2)
        return res


if __name__ == "__main__":
    a = [-2,0]
    sl = Solution()
    print(sl.sortedSquares(a))