def mario(data):
  import re
  import sys
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
    except:
      print('"Научись нормальный код писать уже" - сказал Марио юному программисту.')
      print(sys.exc_info())
  return data
