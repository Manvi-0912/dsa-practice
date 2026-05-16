# Problem: First Unique Character in String
# "leetcode" → 0 (l is first unique)
# "loveleetcode" → 2 (v is first unique)

def first_unique_char(s):
    count = {}

    for char in s:
        count[char] = count.get(char, 0) + 1

    for i, char in enumerate(s):
        if count[char] == 1:
            return i

    return -1

print(first_unique_char("leetcode"))       # 0
print(first_unique_char("loveleetcode"))   # 2
print(first_unique_char("aabb"))           # -1