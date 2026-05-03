# Problem: Find Maximum Element
# Given a list, return the largest number.

def find_maximum(arr):
    maximum = arr[0]  # assume first is biggest

    for num in arr:
        if num > maximum:
            maximum = num  # update if we find bigger

    return maximum

# Test it
print(find_maximum([3, 7, 1, 9, 4]))   # 9
print(find_maximum([100, 2, 50]))       # 100
print(find_maximum([-1, -5, -2]))       # -1