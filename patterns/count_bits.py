# Problem: Number of 1 Bits
# How many 1s are in binary representation?
# 11 = 1011 in binary → three 1s

def count_bits(n):
    count = 0
    while n:
        count += n & 1   # check last bit
        n >>= 1          # shift right
    return count

print(count_bits(11))     # 3  (1011)
print(count_bits(128))    # 1  (10000000)
print(count_bits(255))    # 8  (11111111)