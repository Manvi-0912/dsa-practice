# Problem: Move Zeroes to End
# [0,1,0,3,12] → [1,3,12,0,0]

def move_zeros(nums):
    pos = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[pos], nums[i] = nums[i], nums[pos]
            pos += 1
    return nums

print(move_zeros([0,1,0,3,12]))    # [1,3,12,0,0]
print(move_zeros([0,0,1]))         # [1,0,0]
print(move_zeros([1,2,3]))         # [1,2,3]