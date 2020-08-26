#
# @lc app=leetcode.cn id=389 lang=python3
#
# [389] 找不同
#
# https://leetcode-cn.com/problems/find-the-difference/description/
#
# algorithms
# Easy (62.50%)
# Likes:    151
# Dislikes: 0
# Total Accepted:    33.5K
# Total Submissions: 53.5K
# Testcase Example:  '"abcd"\n"abcde"'
#
# 给定两个字符串 s 和 t，它们只包含小写字母。
# 
# 字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。
# 
# 请找出在 t 中被添加的字母。
# 
# 
# 
# 示例:
# 
# 输入：
# s = "abcd"
# t = "abcde"
# 
# 输出：
# e
# 
# 解释：
# 'e' 是那个被添加的字母。
# 
# 
#

# @lc code=start
from collections import defaultdict
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_dict = defaultdict(int)
        t_dict = defaultdict(int)
        for i in s:
            s_dict[i] += 1
        for j in t:
            t_dict[j] += 1
        #若添加已经存在的字母
        if len(s_dict) == len(t_dict):
            for i in s_dict:
                if s_dict[i] != t_dict[i]:
                    return i
        #若添加了新的字母
        else:
            for i in t_dict:
                if i not in s_dict:
                    return i
# @lc code=end

