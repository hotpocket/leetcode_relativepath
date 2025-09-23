
def iterateLines(callback):
  with open('sowpods.txt','r') as fh:
    try:
      for line in fh:
        line = line.strip()
        callback(line)
    except BrokenPipeError:
      pass # don't complain on things like `python q1.py | head`
