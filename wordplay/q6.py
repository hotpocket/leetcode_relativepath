
# What are all of the words that have a B and an X and are less than 5 letters long?
from utils import iterateLines

def processLine(line):
  if "B" in line and "X" in line and len(line) < 5:
    print(line)


iterateLines(processLine)