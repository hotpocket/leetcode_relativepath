
# What are all of the words that contain the word CAT and are exactly 5 letters long?


with open('sowpods.txt', 'r') as fh:
  for line in fh:
    line = line.strip()
    if "CAT" in line and len(line) == 5:
      print(line)