# вывод строчных букв
def ant_man(data):
  import sys
  if type(data).__name__ == 'str':
   data = data.lower()
  else:
    if type(data).__name__ == 'DataFrame':
      categorical_features = data.select_dtypes(include = ["object"]).columns
      for col in categorical_features:
        if data[col] is not None:
          data[col] = data[col].str.lower()
        else:
          pass
          print(sys.exc_info())
    else:
      print('"Научись нормальный код писать уже" - сказал Человек-Муравей юному программисту.')
      print(sys.exc_info())
  return data
