# Problem: Count Vowels in a String

def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

print(count_vowels("Hello World"))   # 3
print(count_vowels("Python"))        # 1
print(count_vowels("aeiou"))         # 5