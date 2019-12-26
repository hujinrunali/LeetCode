#题目描述：假设有打乱顺序的一群人站成一个队列。 每个人由一个整数对(h, k)表示，其中h是这个人的身高，
# k是排在这个人前面且身高大于或等于h的人数。 编写一个算法来重建这个队列。
#实例：
#输入:[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
#输出:[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
#1.先排序，再插入
#假设候选队列为 A，已经站好队的队列为 B.
#从 A 里挑身高最高的人 x 出来，插入到 B. 因为 B 中每个人的身高都比 x 要高，因此 x 插入的位置，就是看 x 前面应该有多少人就行了。
# 比如 x 前面有 5 个人，那 x 就插入到队列 B 的第 5 个位置。

class Solution:
    def reconstructQueue(self, people):
        datalen = len(people)
        if datalen < 2:
            return people
        people.sort(key=lambda x : [-x[0],x[1]])
        res = []
        for i in range(datalen):
            res.insert(people[i][1],people[i])
        return res

if __name__ == "__main__":
    sl = Solution()
    people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
    print(sl.reconstructQueue(people))
