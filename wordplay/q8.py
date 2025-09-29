# What are all of the words with no vowel and not even a Y?

with open('sowpods.txt') as fh:
    for line in fh:
        line = line.strip()
        if 'A' not in line and 'E' not in line and 'I' not in line and 'O' not in line and 'U' not in line and 'Y' not in line:
            print(line)