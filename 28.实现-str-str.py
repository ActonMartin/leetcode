#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现 strStr()
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        index = haystack.find(needle)
        return index

class Solution2:
    def strStr(self, haystack: str, needle: str) -> int:
        L, n = len(needle), len(haystack)
        if L == 0:
            return 0
        # pn是haystack上的索引，pl是needle上的索引。
        pn = 0
        while pn < n - L + 1:
            # find the position of the first needle character
            # in the haystack string
            while pn < n - L + 1 and haystack[pn] != needle[0]:
                pn += 1
            
            # compute the max match string
            curr_len = pL = 0
            while pL < L and pn < n and haystack[pn] == needle[pL]:
                pn += 1
                pL += 1
                curr_len += 1
            
            # if the whole needle string is found,
            # return its start position
            if curr_len == L:
                return pn - L
            
            # otherwise, backtrack
            pn = pn - curr_len + 1
            
        return -1


# Solution3是自己写的方法，跟Solution2的思想是一样的。但是最后有一些问题
# 主要是后来的flag会出现跳的现象，没有准确的记录第一个符合的位置
class Solution3:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        len_haystack = len(haystack)
        len_needle = len(needle)
        i, j, count_ = 0, 0, 0
        flag = []
        while i < len_haystack:
            if haystack[i] == needle[j]:
                flag.append(i)
                i, j = i+1, j+1
                count_ += 1
            else:
                i += 1
                if flag:
                    if i - flag[0] == len_needle and count_ < len_needle:
                        i = flag[0] + 1
                        flag = []
                j = 0
                count_ = 0
            if count_ == len_needle:
                print(i-len_needle)
                return i-len_needle
        print('-1')
        return -1
# @lc code=end

