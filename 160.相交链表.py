#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution1:
    """ 会出现超时 """
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        list_a, list_b = [],[]
        while headA:
            cur_value = headA
            list_a.append(cur_value)
            headA = headA.next
        while headB:
            cur_value = headB
            list_b.append(cur_value)
            headB = headB.next
        a = [x for x in list_a if x in list_b]
        if len(a) == 0:
            return None
        return a[0]

class Solution2:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        A = set()
        cur1 = headA
        cur2 = headB
        while cur1:
            A.add(cur1)
            cur1 = cur1.next
        while cur2:
            if cur2 in A:
                return cur2
            cur2 = cur2.next
        return None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        cur1 = headA
        cur2 = headB
        while cur1 != cur2:
            cur1 = cur1.next if cur1 else headB
            cur2 = cur2.next if cur2 else headA
        return cur1

# @lc code=end

