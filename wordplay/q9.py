# What are all of the words that have all 5 vowels, in any order?

with open('sowpods.txt') as fh:
    for line in fh:
        line = line.strip()
        if 'A' in line and 'E' in line and 'I' in line and 'O' in line and 'U' in line and 'Y' in line:
            print(line)