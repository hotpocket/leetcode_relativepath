
# What are all of the words that have no E or A and are at least 15 letters long?

with open('sowpods.txt') as fh:
  for line in fh:
    line = line.strip()
    if "E" not in line and "A" not in line and len(line) >= 15:
      print(line)
