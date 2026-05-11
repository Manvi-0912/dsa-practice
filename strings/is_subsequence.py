# Problem: Is Subsequence
# Is "ace" a subsequence of "abcde"? Yes!
# a→b→c→d→e, pick a,c,e → "ace" ✅

def is_subsequence(s, t):
    i = 0
    j = 0

    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1

    return i == len(s)

print(is_subsequence("ace", "abcde"))     # True
print(is_subsequence("aec", "abcde"))     # False
print(is_subsequence("", "abcde"))        # True