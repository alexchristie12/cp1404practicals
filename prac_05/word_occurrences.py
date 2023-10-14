"""
CP1404 Practical 05: Word Occurrences
Estimated Time to Complete: 20 minutes
Actual Time to Complete: 16 minutes
"""

string = input("Text: ")
words = string.split()
word_to_count = {}
for word in words:
    try:
        word_to_count[word] += 1
    except KeyError:
        word_to_count[word] = 1
max_word_length = max((len(word) for word in words))
word_to_count = dict(sorted(word_to_count.items()))
for word in word_to_count:
    print(f"{word:{max_word_length}} : {word_to_count[word]}")
