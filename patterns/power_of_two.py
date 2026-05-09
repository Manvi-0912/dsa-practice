# Problem: Power of Two
# Is a number a power of 2?
# 1,2,4,8,16 → True

def is_power_of_two(n):
    if n <= 0:
        return False
    while n > 1:
        if n % 2 != 0:
            return False
        n = n // 2
    return True

print(is_power_of_two(1))    # True
print(is_power_of_two(16))   # True
print(is_power_of_two(18))   # False