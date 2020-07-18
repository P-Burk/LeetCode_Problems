# Level: Easy
# 1480. Running Sum of 1d Array

# Description:
# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums.

# Example:
# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].


class Solution:
    def runningSum(self, num_list):
        new_list = []
        x = 0
        y = 0
        for i in range(len(num_list)):  # sets number of iterations
            if i == 0:                  # if it's the first iteration....
                y = num_list[i]         # establishes first value as y so that you can add it in else statement
                new_list.append(y)      # adds y (AKA first value) to new list
            else:                       # if not first iteration....
                x = num_list[i] + y     # set x equal to num from input list + y
                new_list.append(x)      # adds the x value to the new list
                y = x                   # sets y equal to x in order to use the x value in line 11 on next iteration
        return new_list


s = Solution()
testCase = [1, 2, 3, 4]
print(s.runningSum(testCase))

# Thoughts:
# To be honest, this is an update to a question I solved a while ago. I don't remember my thoughts on this one other
# than it was fairy easy. I'll have to solve this one again later and give an update.
