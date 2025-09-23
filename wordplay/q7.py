
from utils import iterateLines

# What are all of the words that both start and end with a Y?

def processLine(line: str):
  if line.startswith("Y") and line.endswith("Y"):
    print(line)

iterateLines(processLine)