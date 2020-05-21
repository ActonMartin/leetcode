#
# @lc app=leetcode.cn id=219 lang=python3
#
# [219] 存在重复元素 II
#

# @lc code=start
class Solution1: # Wrong answer
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        len_nums = len(nums)
        for i in range(len(nums)-1):
            max_index = i + k + 1
            if max_index > len_nums:
                max_index = len_nums
            j = i + 1
            while j < max_index + 1 and max_index < len_nums + 1:
                if nums[i] == nums[j]:
                    return True
                else:
                    j += 1
            return False

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        visited = {}
        n = len(nums)
        for i in range(n):
            if nums[i] in visited.keys():
                if i - visited[nums[i]] <= k:
                    return True
                visited[nums[i]] = i
            else:
                visited[nums[i]] = i
        return False
# @lc code=end

