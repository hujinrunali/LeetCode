#题目描述：
# 给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。
#
# 示例 1:
# 输入: 1->2->3->3->4->4->5
# 输出: 1->2->5
#
# 示例 2:
# 输入: 1->1->1->2->3
# 输出: 2->3
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#思路：计算链表中每个元素的个数，个数为1则加入新的链表
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        myhead = ListNode(0)
        mycur = myhead
        cur = head
        while cur:
            value = cur.val
            tmpcur = cur
            count = 0
            while tmpcur and tmpcur.val == value:
                count += 1
                tmpcur = tmpcur.next
            if count == 1:
                mycur.next = cur
                mycur = mycur.next
            cur = tmpcur
        mycur.next = cur
        return myhead.next
