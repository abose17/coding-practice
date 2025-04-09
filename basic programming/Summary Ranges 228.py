# 228. Summary Ranges
# Solved
# Easy
# Topics
# Companies
# You are given a sorted unique integer array nums.

# A range [a,b] is the set of all integers from a to b (inclusive).

# Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

# Each range [a,b] in the list should be output as:

# "a->b" if a != b
# "a" if a == b
 

# Example 1:

# Input: nums = [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]
# Explanation: The ranges are:
# [0,2] --> "0->2"
# [4,5] --> "4->5"
# [7,7] --> "7"
# Example 2:

# Input: nums = [0,2,3,4,6,8,9]
# Output: ["0","2->4","6","8->9"]
# Explanation: The ranges are:
# [0,0] --> "0"
# [2,4] --> "2->4"
# [6,6] --> "6"
# [8,9] --> "8->9"

class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """

        i = len(nums) - 1
        separator=999
        while i > 0:
            # Check if there's a gap between current and previous number
            if nums[i] != nums[i-1] + 1:
                # Insert separator at position i
                nums.insert(i, separator)
            i -= 1
        # print(nums)
        # Split the list by separator
        result = []
        current_sublist = []
    
        for num in nums:
            if num == separator:
                if current_sublist:  # Only append non-empty sublists
                    # print(str(current_sublist[0]) +"->" + str(current_sublist[-1]))
                    if current_sublist[0] != current_sublist[-1]:
                        rangejoin = str(current_sublist[0]) +"->" + str(current_sublist[-1])
                    else:
                        rangejoin = str(current_sublist[0])
                    result.append(rangejoin)
                    current_sublist = []
            else:
                current_sublist.append(num)
        
        # Add the last sublist if it's not empty
        if current_sublist:
            if current_sublist[0] != current_sublist[-1]:
                rangejoin = str(current_sublist[0]) +"->" + str(current_sublist[-1])
            else:
                rangejoin = str(current_sublist[0])
            result.append(rangejoin)
        
        return result

        
