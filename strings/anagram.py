# Problem: Valid Anagram
# Two words are anagrams if they have same letters
# "listen" and "silent" → True

def is_anagram(s, t):
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)

print(is_anagram("listen", "silent"))   # True
print(is_anagram("hello", "world"))     # False
print(is_anagram("rat", "tar"))         # True