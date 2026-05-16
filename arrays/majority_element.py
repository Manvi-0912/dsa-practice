# Problem: Majority Element
# Element that appears more than n/2 times
# [3,2,3] → 3
# Boyer-Moore Voting Algorithm!

def majority_element(nums):
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num
        if num == candidate:
            count += 1
        else:
            count -= 1

    return candidate

print(majority_element([3,2,3]))            # 3
print(majority_element([2,2,1,1,1,2,2]))    # 2
print(majority_element([1]))               # 1