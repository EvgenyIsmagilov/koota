import re
import sys


def mario(data):
  # function eliminate redundant brackets
  if type(data).__name__ == 'str':
    data = data.replace(r'\s+','', regex=True)
  elif type(data).__name__ == 'DataFrame':
    while "  " in data:
      data = data.replace(r'\s+','', regex=True)
  elif type(data).__name__ == 'list':
    for item in data:
      item.replace("'", "")   
  else:
    try:
      data = data.replace(r'\s+','', regex=True)
    except Exception:
      print(sys.exc_info())
  return data
