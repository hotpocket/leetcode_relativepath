# For loops and if conditions
# What are all of the words containing UU?

# iterate lines in file
# if line contains the string "UU" add it to a running list
# print the list

words_file = 'sowpods.txt'
with open(words_file) as fh:
  try:
    for line in fh:
      if "UU" in line:
        print(line.strip())
  except BrokenPipeError:
    pass # don't complain on things like `python q1.py | head`


