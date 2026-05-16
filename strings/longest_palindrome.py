# Problem: Longest Palindrome
# Given letters, what's the longest palindrome you can build?
# "abccccdd" → 7 ("dccaccd")

def longest_palindrome(s):
    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1

    length = 0
    odd_found = False

    for c in count.values():
        length += c // 2 * 2   # use pairs
        if c % 2 == 1:
            odd_found = True   # one odd char can go in middle

    if odd_found:
        length += 1

    return length

print(longest_palindrome("abccccdd"))    # 7
print(longest_palindrome("a"))           # 1
print(longest_palindrome("aabbcc"))      # 6