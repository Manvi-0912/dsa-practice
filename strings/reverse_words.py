# Problem: Reverse Words in a String
# "the sky is blue" → "blue is sky the"

def reverse_words(s):
    words = s.split()
    return ' '.join(reversed(words))

print(reverse_words("the sky is blue"))      # blue is sky the
print(reverse_words("  hello world  "))      # world hello
print(reverse_words("a good   example"))     # example good a