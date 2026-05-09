# Problem: Count Words in a Sentence

def count_words(sentence):
    words = sentence.split()
    return len(words)

print(count_words("Hello my name is Manvi"))   # 5
print(count_words("I love coding"))            # 3
print(count_words("One"))                      # 1