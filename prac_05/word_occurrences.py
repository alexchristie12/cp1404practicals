"""
CP1404 Practical 05: Word Occurrences
Estimated Time to Complete: 20 minutes
Actual Time to Complete:
"""

string = input("Text: ")
words = string.split()
word_to_count = {}
for word in words:
    try:
        word_to_count[word] += 1
    except KeyError:
        word_to_count[word] = 1
print(word_to_count)
