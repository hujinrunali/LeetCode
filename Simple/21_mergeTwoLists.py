#题目描述：
# 两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
#
# 示例：
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    #迭代的方式-创建新结点
    #解题思路：通过两个指针分别指向l1和l2，比较两个结点的元素较小的那个加入新的链表，当其中l1和l2中有一个到达尾结点时，
    # 退出while循环。之后再将没有到达尾结点的链表逐个加入新链表
    #算法时间复杂度分析：算法相等于所有结点都遍历一遍
    #                   假设l1有m个元素，l2有n个元素
    #                   算法的时间复杂度为：O(m+n)
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 :
            return l2
        if not l2:
            return l1
        head = ListNode(0)
        cur = head
        if l1.val > l2.val:
            head.val = l2.val
            l2 = l2.next
        else:
            head.val = l1.val
            l1 = l1.next
        while l1 and l2:
            temp = ListNode(0)
            if l1.val > l2.val:
                temp.val = l2.val
                l2 = l2.next
            else:
                temp.val = l1.val
                l1 = l1.next
            cur.next = temp
            cur = cur.next
        while l1:
            temp = ListNode(0)
            temp.val = l1.val
            l1 = l1.next
            cur.next = temp
            cur = cur.next
        while l2:
            temp = ListNode(0)
            temp.val = l2.val
            l2 = l2.next
            cur.next = temp
            cur = cur.next
        return head

    #采用递归的方式求解
    #时间复杂度分析T(n) = T(n-1)+O(1)
    #时间复杂度为：O(m+n)
    def mergeTwoLists2(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 :
            return l2
        if not l2:
            return l1
        if l1.val > l2.val:
            l2.next = self.mergeTwoLists2(l1,l2.next)
            return l2
        else:
            l1.next = self.mergeTwoLists2(l1.next,l2)
            return l1

    #采用迭代的方式-使用原有结点
    def mergeTwoLists3(self, l1: ListNode, l2: ListNode) -> ListNode:
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
