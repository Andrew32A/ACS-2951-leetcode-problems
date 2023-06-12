# *******************************************************************************
# Question
# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

# You must solve this problem without using the library's sort function.

# Example 1:
# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]

# Example 2:
# Input: nums = [2,0,1]
# Output: [0,1,2]

# *******************************************************************************
# Solution
# 1. If it is 0, we swap it with the element at red_ptr, move both pointers forward, and increment curr_ptr
# 2. If it is 2, we swap it with the element at blue_ptr, move the blue_ptr backward, and do not increment curr_ptr to recheck the swapped element
# 3. If it is 1, we leave it in its place and move curr_ptr forward

class Solution(object):
    def sortColors(self, nums):
        red_ptr, blue_ptr = 0, len(nums) - 1
        curr_ptr = 0

        while curr_ptr <= blue_ptr:
            if nums[curr_ptr] == 0:
                nums[curr_ptr], nums[red_ptr] = nums[red_ptr], nums[curr_ptr]
                red_ptr += 1
                curr_ptr += 1
            elif nums[curr_ptr] == 2:
                nums[curr_ptr], nums[blue_ptr] = nums[blue_ptr], nums[curr_ptr]
                blue_ptr -= 1
            else:
                curr_ptr += 1

# Test the solution
nums = [2, 0, 2, 1, 1, 0]
solution = Solution()
solution.sortColors(nums)
print(nums)  # Output: [0, 0, 1, 1, 2, 2]

nums = [2, 0, 1]
solution.sortColors(nums)
print(nums)  # Output: [0, 1, 2]

# Time Complexity: O(n)
# Space Complexity: O(1)
