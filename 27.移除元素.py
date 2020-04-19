#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
class Solution3:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:return 0
        slow = 0   
        n = len(nums)
        fast = n - 1
        while slow < fast:
            while slow < fast and nums[slow] != val:
                slow += 1
            while slow < fast and nums[fast] == val:
                fast -= 1
            nums[slow],nums[fast] = nums[fast],nums[slow]
            #slow += 1
            #fast -= 1
        res = 0
        #print(nums,slow,fast)
        #return fast + 1
        for i in range(n):
            if nums[i] == val:
                return res
            res += 1

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for j in range(len(nums)):
            if nums[j]!= val:
                nums[i] = nums[j]
                i+=1
        return i 
'''
class Solution1:
    def removeElement(self, nums: List[int], val: int) -> int:
        length = len(nums)
        count = 0
        for i in range(length):
            if nums[i] == val:
                count+=1
        while count:
            nums.remove(val)
            count-=1 
        return len(nums)  
'''             
# @lc code=end

