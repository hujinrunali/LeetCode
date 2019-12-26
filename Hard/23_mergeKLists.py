#题目描述：
# 合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。
#
# 示例:
# 输入:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# 输出: 1->1->2->3->4->4->5->6
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    #暴力解法
    #将链表转换成数组，再排序合并
    #时间复杂度分析：遍历了链表列表的所有结点，时间复杂度为O(kN)
    def mergeKLists(self, lists) -> ListNode:
        if not lists:
            return None
        else:
            mylist = []
            for l in lists:
                while l:
                    mylist.append(l.val)
                    l = l.next
            mylist.sort()
            head = ListNode(-1)
            cur = head
            for val in mylist:
                temp = ListNode(val)
                cur.next = temp
                cur = cur.next
            return head.next

    #逐次比较
    def mergeKLists2(self, lists) -> ListNode:
        datalen = len(lists)
        if not lists or datalen == 0 :
            return None
        else:
            head = ListNode(-1)
            cur = head
            mynode = None
            datalen = len(lists)
            countNode = 0
            while countNode < datalen:
                mynode = 0
                minval = float('inf')
                for i in range(datalen):
                    if lists[i] and lists[i].val < minval:
                        minval = lists[i].val
                        mynode = i
                #特殊情况[[]]-需要在此处特意处理
                if not lists[mynode]:
                    break
                cur.next = lists[mynode]
                cur = cur.next
                lists[mynode] = lists[mynode].next
                if not lists[mynode]:
                    countNode += 1
            return head.next
    # 通过两两合并的方式
    #算法缺点：时间复杂度过大
    def mergeKLists3(self, lists) -> ListNode:
        if not lists :
            return None
        datalen = len(lists)
        if datalen == 1:
            return lists[0]

        pre = lists[0]
        for i in range(1,datalen):
            pre = self.mergeTwoLists(pre,lists[i])
        return pre

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(-1)
        cur = head
        while l1 and l2:
            if l1.val > l2.val:
                cur.next = l2
                l2 = l2.next
            else:
                cur.next = l1
                l1 = l1.next
            cur = cur.next
        cur.next = l1 if l1 else l2
        #返回不带头结点的链表
        return head.next

    # 采用分治算法

    def mergeKLists4(self, lists) -> ListNode:
        if not lists :
            return None
        datalen = len(lists)
        if datalen == 1:
            return lists[0]
        if datalen == 2:
            return self.mergeTwoLists(lists[0],lists[1])
        mid = datalen//2
        left = self.mergeKLists4(lists[0:mid])
        right = self.mergeKLists4(lists[mid:])
        return self.mergeTwoLists(left,right)

    # 采用改进的分治算法
    # 此算法执行最快，占用内存最少,此算法避免了重复的计算
    def mergeKLists5(self, lists) -> ListNode:
        if not lists :
            return None
        datalen = len(lists)
        if datalen == 1:
            return lists[0]
        interval= 1
        while interval < datalen:
            for i in range(0,datalen-interval,interval*2):
                lists[i] = self.mergeTwoLists(lists[i],lists[i+interval])
            interval *= 2
        return lists[0]

if __name__ == '__main__':
    head1 = ListNode(1)
    head1.next = ListNode(4)
    head1 = head1.next
    head1.next = ListNode(5)

    head2 = ListNode(1)
    head2.next = ListNode(3)
    head2 = head2.next
    head2.next = ListNode(4)

    head3 = ListNode(2)
    head3.next = ListNode(6)

    mylist = [head1,head2,head3]

    sl = Solution()
    head = sl.mergeKLists2(mylist)
    while head:
        print(head.val,end=" ")
        head = head.next