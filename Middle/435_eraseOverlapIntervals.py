#题目描述：给定一个区间的集合，找到需要移除区间的最小数量，使剩余区间互不重叠。
#实例：输入: [ [1,2], [2,3], [3,4], [1,3] ]
#输出: 1
#解释: 移除 [1,3] 后，剩下的区间没有重叠。
class Solution:
    def eraseOverlapIntervals(self, intervals) -> int:
        datalen = len(intervals)
        if datalen < 2:
            return intervals
        intervals.sort(key=lambda x : [x[0],x[1]-x[0]])
        res = 0
        totaltravel = 1
        i = 1
        while True:
            if intervals[i][0] < intervals[i-1][1]:
                intervals.pop(i)
                res += 1
            else:
                i += 1
            totaltravel += 1
            if totaltravel >= datalen:
                break
        return res


if __name__ == "__main__":
    sl = Solution()
    intervals = [[1,5], [2,3], [3,4], [1,3]]
    print(sl.eraseOverlapIntervals(intervals))









