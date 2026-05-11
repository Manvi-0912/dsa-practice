# Problem: Count occurrences of each element

def count_occurrences(nums):
    count = {}
    for num in nums:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    return count

print(count_occurrences([1,2,2,3,3,3]))    # {1:1, 2:2, 3:3}
print(count_occurrences([4,4,4,4]))        # {4:4}
print(count_occurrences([1,2,3]))          # {1:1, 2:1, 3:1}