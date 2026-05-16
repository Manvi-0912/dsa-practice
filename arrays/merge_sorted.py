# Problem: Merge Two Sorted Arrays
# [1,3,5] + [2,4,6] → [1,2,3,4,5,6]

def merge_sorted(arr1, arr2):
    result = []
    i = j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    result.extend(arr1[i:])
    result.extend(arr2[j:])
    return result

print(merge_sorted([1,3,5], [2,4,6]))      # [1,2,3,4,5,6]
print(merge_sorted([1,2,3], [4,5,6]))      # [1,2,3,4,5,6]
print(merge_sorted([1,5,9], [2,3,10]))     # [1,2,3,5,9,10]