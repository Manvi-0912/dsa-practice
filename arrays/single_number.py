# Problem: Single Number
# Every number appears twice except one
# [4,1,2,1,2] → 4

def single_number(nums):
    result = 0
    for num in nums:
        result ^= num   # XOR trick!
    return result

print(single_number([2,2,1]))        # 1
print(single_number([4,1,2,1,2]))    # 4
print(single_number([1]))            # 1