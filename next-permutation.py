
# *******************************************************************************
# Question
# Given an array of integers nums, find the next permutation of nums.
# A permutation of an array of integers is an arrangement of its members into a sequence or linear order. The next permutation of an array of integers is the next lexicographically greater permutation of its integers.
# If such an arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

# Example 1:
# Input: nums = [1,2,3]
# Output: [1,3,2]
# Explanation: The next permutation of [1,2,3] is [1,3,2].

# Example 2:
# Input: nums = [3,2,1]
# Output: [1,2,3]
# Explanation: [3,2,1] does not have a lexicographical larger rearrangement, so the next permutation is the lowest possible order, which is [1,2,3].

# *******************************************************************************
# Solution
# The problem can be solved using the following steps:
# 1. Start from the rightmost element of the array and find the first pair of adjacent elements nums[i] and nums[i-1] where nums[i] > nums[i-1].
# 2. If such a pair is found, it means that the current permutation can be rearranged to get the next lexicographically greater permutation.
# 3. To find the next permutation, we need to swap the element nums[i-1] with the smallest element in the subarray nums[i:] that is greater than nums[i-1]. This ensures that the new permutation is greater than the current permutation but still the smallest possible.
# 4. After swapping, we reverse the subarray nums[i:] to make it the lowest possible order.
# 5. If no such pair is found in step 1, it means that the array is already sorted in descending order, and there is no next permutation possible. In this case, we reverse the entire array to get the lowest possible order.

class Solution(object):
    def nextPermutation(self, nums):
        i = len(nums) - 1
        while i > 0 and nums[i] <= nums[i-1]:
            i -= 1
        
        if i > 0:
            j = len(nums) - 1
            while nums[j] <= nums[i-1]:
                j -= 1
            nums[i-1], nums[j] = nums[j], nums[i-1]
        
        left = i
        right = len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        
        return nums

# Test case 1
nums1 = [1,2,3]
solution = Solution()
result1 = solution.nextPermutation(nums1)
print(result1)

# Test case 2
nums2 = [3,2,1]
result2 = solution.nextPermutation(nums2)
print(result2)


# Time Complexity: O(n), where n is the length of the input array nums.
# Space Complexity: O(1)
# Explanation:
# The solution starts from the rightmost element and scans towards the left to find the first pair of adjacent elements where the left element is smaller than the right element. This step is done in O(n) time.
# If such a pair is found, the solution swaps the left element with the smallest element in the subarray that is greater than the left element. This is done in O(n) time in the worst case, as the solution scans the subarray from right to left.
# Finally, the solution reverses the subarray to the right of the swapped element. This step also takes O(n) time in the worst case.
# Hence, the overall time complexity of the solution is O(n).
# The space complexity of the solution is O(1) as it uses only a constant amount of extra space to store the indices and temporary variables.