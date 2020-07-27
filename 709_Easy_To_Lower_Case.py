# Level: Easy
# 709. To Lower Case

# Description:
# Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

# Example 1:
# Input: "Hello"
# Output: "hello"

# Example 2:
# Input: "here"
# Output: "here"


class Solution:
    def toLowerCase(self, input_string):
        return input_string.lower()


testCase = 'LOVELY'
s = Solution()
print(s.toLowerCase(testCase))

# Thoughts:
# Very basic case change for strings. Took all of 15 seconds to come up with and code the answer.
