
# What are all of the words containing a Q but not a U?

with open('sowpods.txt', 'r') as fh:
  for line in fh:
    if "Q" in line and "U" not in line:
      print(line.strip())

