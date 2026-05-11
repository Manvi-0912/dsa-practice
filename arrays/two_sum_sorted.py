# Problem: Two Sum in Sorted Array
# Use two pointers instead of hashmap

def two_sum_sorted(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        total = nums[left] + nums[right]
        if total == target:
            return [left, right]
        elif total < target:
            left += 1
        else:
            right -= 1

    return []

print(two_sum_sorted([2,7,11,15], 9))    # [0,1]
print(two_sum_sorted([1,3,4,5,7], 9))    # [2,3]
print(two_sum_sorted([1,2,3,4,5], 6))    # [0,4]