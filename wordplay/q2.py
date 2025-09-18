# What are all of the words containing an X and a Y and a Z?

# check if x and y and z are in sowpods

words_file = 'sowpods.txt'
with open(words_file) as fh:
    for line in fh:
        if 'X' in line and 'Y' in line and 'Z' in line:
            print(line.strip())