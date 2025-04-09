# 209. Minimum Size Subarray Sum
# Attempted
# Medium
# Topics
# Companies
# Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

# Example 1:

# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.
# Example 2:

# Input: target = 4, nums = [1,4,4]
# Output: 1
# Example 3:

# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0

class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        print("nums-> ", nums)
        sum = 0
        count = 1
        for i in range(len(nums)-1, -1, -1):
            sum = sum + nums[i]
            if sum >= target:
                return count
            count += 1
        return 0 

        