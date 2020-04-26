#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [*filter(str.isalnum, s.lower())] 
        return s == s[::-1]

import re
import time
class Solution2:
    '''
    经过测试，先给字符串转换为小写，
    再去正则化花费时间短一些
    '''
    def isPalindrome(self, s: str) -> bool:
        start_time = time.time()
        p = ''.join(re.findall(r'[a-zA-Z0-9]+',s.lower()))
        #p = p.lower()
        end_time = time.time()
        print(end_time - start_time)
        return True if p==p[::-1] else False
# @lc code=end

