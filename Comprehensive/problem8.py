# Problem: Find the First Pair that Sums to a Target
# Description:
# Given an array of integers nums and an integer target, find the first pair of numbers that add up to the target. Return these two numbers.

# Input:
# nums: An array of integers.
# target: An integer.
# Output:

# Return the first pair of numbers that add up to the target in the form of a list.

def find_pair(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [nums[i], nums[j]]
    return []

nums = [1, 2, 3, 4, 5, 6]
target = 11
result = find_pair(nums, target)
print(result)
