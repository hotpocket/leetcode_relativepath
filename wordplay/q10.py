# What are all of the words that have all 5 vowels, in alphabetical order?

# find all words with all vowels

# acii value?
# ord or ch 
# if a word has vowels, is it one of vowel? 
#'yaeiouy' this will not meeet the criteria
# create a list or dict to hold the word that contain all vowels

result_all_words_with_all_vowels_in_order = []

with open('sowpods.txt') as fh:
    for line in fh:
        word = line.strip()
        if 'A' in word and 'E' in word and 'I' in word and 'O' in word and 'U' in word and 'Y' in word:
            # extract all of the vowels in the order they appear in the word into a list
            vowel_values = []
            for i,char in enumerate(word):
                if 'A' == char or 'E' == char or 'I' == char or 'O' == char or 'U' == char or 'Y'== char:
                    # convert those vowels in the list to their corresponding number
                    vowel_values.append(ord(char))
            # create a copy of the list whose values are sorted
            sorted_vowel_values = sorted(vowel_values)
            # compare the two lists -- test
            if sorted_vowel_values == vowel_values:
                print(word)
        