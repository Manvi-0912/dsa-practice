# Problem: Binary Search
# Find a number in a SORTED list fast
# Instead of checking every element, cut list in half each time

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid        # found it! return position
        elif arr[mid] < target:
            left = mid + 1    # search right half
        else:
            right = mid - 1   # search left half

    return -1   # not found

print(binary_search([1,3,5,7,9,11], 7))    # 3
print(binary_search([1,3,5,7,9,11], 6))    # -1
print(binary_search([2,4,6,8,10], 10))     # 4