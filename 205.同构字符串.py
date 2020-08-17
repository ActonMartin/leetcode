#
# @lc app=leetcode.cn id=205 lang=python3
#
# [205] 同构字符串
#
# https://leetcode-cn.com/problems/isomorphic-strings/description/
#
# algorithms
# Easy (47.30%)
# Likes:    227
# Dislikes: 0
# Total Accepted:    48.1K
# Total Submissions: 101.6K
# Testcase Example:  '"egg"\n"add"'
#
# 给定两个字符串 s 和 t，判断它们是否是同构的。
# 
# 如果 s 中的字符可以被替换得到 t ，那么这两个字符串是同构的。
# 
# 所有出现的字符都必须用另一个字符替换，同时保留字符的顺序。两个字符不能映射到同一个字符上，但字符可以映射自己本身。
# 
# 示例 1:
# 
# 输入: s = "egg", t = "add"
# 输出: true
# 
# 
# 示例 2:
# 
# 输入: s = "foo", t = "bar"
# 输出: false
# 
# 示例 3:
# 
# 输入: s = "paper", t = "title"
# 输出: true
# 
# 说明:
# 你可以假设 s 和 t 具有相同的长度。
# 
#

# @lc code=start
class Solution1:
    """ 这个方法有问题，无法记忆顺序 """
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_set = set(s)
        t_set = set(t)
        s_count_list, t_count_list = [], []
        for i in s_set:
            s_count_list.append(s.count(i))
            s_count_list= sorted(s_count_list)
        for i in t_set:
            t_count_list.append(t.count(i))
            t_count_list = sorted(t_count_list)
        if len(s_set) == len(t_set) and s_count_list == t_count_list:
            return True
        else:
            return False

class Solution2:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return [*map(s.index, s)] == [*map(t.index, t)]

class Solution:
    """ 如果s的长度和t的长度不一样，返回false
    遍历s:利用哈希表
    如果s[i]不在哈希表中，需要考虑两种情况，如果t[i]在哈希表的value中，返回false,
                        否则返回hashtable[s[i]] = t[i]
    如果s[i]在哈希表中，如果hashtable[s[i]]!=t[i],则返回false
    """
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        hashtable={}
        for i in range(len(s)):
            if s[i] not in hashtable:
                if t[i] in list(hashtable.values()):
                    return False
                else:
                    hashtable[s[i]]=t[i]
            else:
                if hashtable[s[i]] != t[i]:
                    return False
        print(hashtable)
        return True
            

# @lc code=end

