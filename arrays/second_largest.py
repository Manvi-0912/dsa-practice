# Problem: Find Second Largest Element

def second_largest(arr):
    first = second = float('-inf')
    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    return second

print(second_largest([3, 7, 1, 9, 4]))   # 7
print(second_largest([10, 5, 8]))         # 8
print(second_largest([1, 1, 1, 2]))       # 1