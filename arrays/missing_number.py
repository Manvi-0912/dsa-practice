# Problem: Missing Number
# Given list [0,1,2,4,5] find the missing number (3)

def missing_number(nums):
    n = len(nums)
    expected = n * (n + 1) // 2  # sum of 0 to n
    return expected - sum(nums)

print(missing_number([0, 1, 2, 4, 5]))   # 3 (wait, this is wrong)
print(missing_number([3, 0, 1]))          # 2
print(missing_number([0, 1]))             # 2