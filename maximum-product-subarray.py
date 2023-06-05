# *******************************************************************************
# Question
# Given an integer array nums, find a subarray that has the largest product, and return the product.

# Example 1:
# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.

# Example 2:
# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

# *******************************************************************************
# Solution
# 1. Define a function called "maxProduct" that takes a list of integers "nums" as input.
# 2. Initialize variables "max_prod", "min_prod", and "result" to store the maximum product, minimum product, and final result, respectively.
# 3. Set "max_prod" and "min_prod" to the first element of "nums".
# 4. Set "result" to "max_prod".
# 5. Iterate through "nums" starting from the second element:
#    - Calculate the new "max_prod" by taking the maximum value among "max_prod * nums[i]", "min_prod * nums[i]", and "nums[i]".
#    - Calculate the new "min_prod" by taking the minimum value among "max_prod * nums[i]", "min_prod * nums[i]", and "nums[i]".
#    - Update "result" to be the maximum value between "result" and "max_prod".
# 6. Return "result".

def maxProduct(nums):
    if not nums:
        return 0

    max_prod = min_prod = result = nums[0]

    for i in range(1, len(nums)):
        temp_max = max_prod
        max_prod = max(max_prod * nums[i], min_prod * nums[i], nums[i])
        min_prod = min(temp_max * nums[i], min_prod * nums[i], nums[i])
        result = max(result, max_prod)

    return result

nums = [2,3,-2,4]
print(maxProduct(nums))  # 6

nums = [-2,0,-1]
print(maxProduct(nums))  # 0

# Time complexity: O(n)
# Space complexity: O(1)