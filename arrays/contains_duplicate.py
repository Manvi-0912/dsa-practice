# Problem: Contains Duplicate
# Return True if any number appears twice

def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

print(contains_duplicate([1,2,3,1]))      # True
print(contains_duplicate([1,2,3,4]))      # False
print(contains_duplicate([1,1,1,3,3]))    # True