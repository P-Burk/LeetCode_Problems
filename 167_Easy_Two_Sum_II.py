# Level: Easy
# 167. Two Sum II - Input array is sorted

# Description:
# Given an array of integers that is already sorted in ascending order,
# find two numbers such that they add up to a specific target number.
# The function twoSum should return indices of the two numbers such that they add up to the target,
# where index1 must be less than index2.

# Note:
# Your returned answers (both index1 and index2) are not zero-based.
# You may assume that each input would have exactly one solution and you may not use the same element twice.

# Example:
# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.


class Solution:
    def twoSum(self, num_list, target):
        dict1 = {}
        for pos, num in enumerate(num_list):
            compliment = target - num
            if compliment not in dict1:
                dict1[num] = pos
            else:
                return [(dict1[compliment]+1), (pos+1)]


s = Solution()
testCase = [2, 7, 11, 15]
testTarget = 9
print(s.twoSum(testCase, testTarget))


# Thoughts:
# For this one, I literally just took my answer for LC question #1 and added "+1" to the outputs in line 30.
# I'm not sure if this is the best way because it seems like it's so obvious that it has to be wrong.
# But hey, it works.

