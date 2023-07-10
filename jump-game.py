# *******************************************************************************
# Question
# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
# Return true if you can reach the last index, or false otherwise.

# Example 1:
# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

# Example 2:
# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

# *******************************************************************************
# Solution
# The problem can be solved using a greedy approach. We can start from the first index and iterate through the array, keeping track of the maximum reachable index so far. If at any point the current index is greater than the maximum reachable index, it means we cannot reach the last index and we return False. Otherwise, if we successfully reach the last index, we return True.

class Solution(object):
    def canJump(self, nums):
        maxReachable = 0  # maximum reachable index so far

        for i in range(len(nums)):
            if i > maxReachable:
                return False
            maxReachable = max(maxReachable, i + nums[i])

        return True


# Test case 1
nums1 = [2, 3, 1, 1, 4]
solution = Solution()
result1 = solution.canJump(nums1)
print(result1)

# Test case 2
nums2 = [3, 2, 1, 0, 4]
result2 = solution.canJump(nums2)
print(result2)

# Time Complexity: O(n), where n is the length of the input array nums.
# Space Complexity: O(1)
# Explanation:
# The solution iterates through the array from left to right, keeping track of the maximum reachable index so far (maxReachable).
# If at any point the current index is greater than maxReachable, it means we cannot reach the last index, so the solution returns False.
# Otherwise, the solution updates maxReachable by taking the maximum between the current maxReachable and the sum of the current index and the jump length at that index (i + nums[i]).
# After iterating through the array, if we have successfully reached the last index (i.e., maxReachable is greater than or equal to the last index), the solution returns True.
# The time complexity of the solution is O(n) because it iterates through the array once.
# The space complexity of the solution is O(1) as it uses only a constant amount of extra space to store the maxReachable variable.