# Problem: Reverse a String

def reverse_string(s):
    left = 0
    right = len(s) - 1
    s = list(s)
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return ''.join(s)

print(reverse_string("hello"))      # olleh
print(reverse_string("Manvi"))      # ivnaM
print(reverse_string("python"))     # nohtyp