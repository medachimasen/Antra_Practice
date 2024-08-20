# list of common words (source: Collins Dictionary)
common_words = ("the", "of", "and", "a", "to", \
    "in", "is", "you", "that", "it", "he", \
    "was", "for", "on", "are", "as", "with", "his", \
    "they", "I", "at", "be", "this", "have", "from")

# how many are there?
title = "A - Number of words"
print("\n" + title + "\n" + "-" * len(title))
print(len(common_words))

# show the first 5 words
title = "B - First 5 words"
print("\n" + title + "\n" + "-" * len(title))
print(common_words[:5])

# the last 3 words
title = "C - Last 3 words"
print("\n" + title + "\n" + "-" * len(title))
print(common_words[-3:])

# every fifth word
title = "D - Every 5th word"
print("\n" + title + "\n" + "-" * len(title))
print(common_words[::5])

# iterate over words, listing out the ones with four letters
title = "E - Four-letter words"
print("\n" + title + "\n" + "-" * len(title))

for word in common_words:

    # for each word, if it's length is 4 characters, print it
    if len(word) == 4:
        print(word)

# words beginning with W
title = "F - Words starting with W"
print("\n" + title + "\n" + "-" * len(title))

for each_word in common_words:

    # if lower case version starts with W, print it
    if each_word.lower().startswith("w"):
        print(each_word)


# show the words in alphabetical order (need to convert to a list first)
title = "G - Words in order"
print("\n" + title + "\n" + "-" * len(title))
list_words = list(common_words)
list_words.sort()
print(list_words)