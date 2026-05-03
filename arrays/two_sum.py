# Problem: Two Sum
# Link: https://leetcode.com/problems/two-sum/
# Given a list of numbers and a target,
# return positions of two numbers that add up to target.

def two_sum(nums, target):
    seen = {}  # stores number and its position

    for i in range(len(nums)):
        need = target - nums[i]  # what number do we need?

        if need in seen:
            return [seen[need], i]  # found it!

        seen[nums[i]] = i  # save this number and position

# Test it
print(two_sum([2, 7, 11, 15], 9))   # should print [0, 1]
print(two_sum([3, 2, 4], 6))        # should print [1, 2]
print(two_sum([3, 3], 6))           # should print [0, 1]