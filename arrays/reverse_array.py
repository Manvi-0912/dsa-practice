# Problem: Reverse an Array
# Example: [1,2,3,4,5] → [5,4,3,2,1]

def reverse_array(arr):
    left = 0
    right = len(arr) - 1
    
    while left < right:
        # swap
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    
    return arr

# Test it
print(reverse_array([1, 2, 3, 4, 5]))