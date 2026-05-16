# Problem: Happy Number
# 19 → 1²+9²=82 → 8²+2²=68 → 6²+8²=100 → 1²+0²+0²=1 → Happy!

def is_happy(n):
    seen = set()

    while n != 1:
        if n in seen:
            return False   # cycle detected → not happy
        seen.add(n)
        n = sum(int(d)**2 for d in str(n))

    return True

print(is_happy(19))     # True
print(is_happy(2))      # False
print(is_happy(7))      # True