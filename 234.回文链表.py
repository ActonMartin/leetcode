#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#
# https://leetcode-cn.com/problems/palindrome-linked-list/description/
#
# algorithms
# Easy (42.98%)
# Likes:    606
# Dislikes: 0
# Total Accepted:    117.5K
# Total Submissions: 272.8K
# Testcase Example:  '[1,2]'
#
# 请判断一个链表是否为回文链表。
# 
# 示例 1:
# 
# 输入: 1->2
# 输出: false
# 
# 示例 2:
# 
# 输入: 1->2->2->1
# 输出: true
# 
# 
# 进阶：
# 你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution1:
    """ have some problems """
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return True
        # 计算长度
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        
        # 取出后半部分
        length1 = length //2 if length % 2 == 0 else (length-1) // 2
        new = head
        while length1 > 0:
            new = new.next
            length1 -= 1
        
        # 反转后半部分
        prev = None
        while new:
            temp = new.next
            new.next = prev
            prev = new
            new = temp
        
        # 与前半部分逐项对比
        prev_c, head_c = prev, head
        while prev_c:
            if prev_c.val != head.val:
                return False
            prev_c = prev_c.next
            head_c = head_c.next
        return True

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow,fast,prev = head,head,None
        while fast is not None:
            slow = slow.next
            fast = fast.next.next if fast.next is not None else fast.next
        while slow is not None:
            # slow.next, slow, prev= prev, slow.next, slow
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        while head and prev:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next
        return True

# @lc code=end

