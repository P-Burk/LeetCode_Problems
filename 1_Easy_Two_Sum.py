# Level: Easy
# 1. Two Sum

# Description:
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example:
# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9, return [0, 1].


class Solution:
    def twoSum(self, nums_list, target):
        dict1 = {}                              # create blank dictionary
        for pos, num in enumerate(nums_list):   # enumerate through the list. pos = position in list, num = number from list
            x = target - num                    # finds the compliment of the number from the list. compliment + number = target
            if x not in dict1:                  # looks for the compliment in the dictionary, if not found.....
                dict1[num] = pos                # adds the number as the key and the position as the value to the dictionary
            else:                               # if found.....
                return [dict1[x], pos]          # returns the value (AKA position) of the complement and the position of the current enumeration from line 16


s = Solution()
list1 = [2, 7, 11, 15]
target1 = 9
print(s.twoSum(list1, target1))

# Pay attention to line 19. You want the number to be the KEY and the position to be the VALUE.
# This way your return statement returns the VALUE of KEY x
