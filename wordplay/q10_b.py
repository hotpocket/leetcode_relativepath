######
# What are all of the words that have all 5 vowels, in alphabetical order?
# Find all words with all vowels.
######

# functions used: all, strip, sorted, open, print

# if a word has all of the vowels, are the in order?
#'yaeiouy' this will not meeet the criteria

vowels = ['A','E','I','O','U','Y']

with open('sowpods.txt') as fh:
    for line in fh:
        word = line.strip()
        # check if the word contains all vowels
        if all(vowel in word for vowel in vowels):
            # grab just the vowels in the word in the order they appear
            word_vowels = [char for char in word if char in vowels]
            # if the vowels are in alphebetical order in the word,
            # their sorted value should be the same as the original
            if sorted(word_vowels) == word_vowels:
                print(word)
