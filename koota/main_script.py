# Замечания
# - Надо лучше определить формат float

import pandas as pd
import numpy as np
import sys

# class AnimeTeam:
  # def __init__(self):
  #   self.data = [] #temp


def memory_measure(df):
  return round(df.memory_usage().sum() / 1024**2, 2)


def any_floats(df, col_name):
  return any(isinstance(number, float) for number in set(df[col_name].dropna()))


def check_set_contains_list(some_set, some_list):
  return all(number in some_set for number in some_list)


def bool_check(self, df, col_name):
  self.condition_1 = df[col_name].dtype == 'bool'
  self.df_sample = set(df[col_name].dropna().sample(100))
  self.boll_list_1 = (True, False)
  self.boll_list_2 = (1, 0)
  self.condition_2 = (len(self.df_sample) <= 2) & (check_set_contains_list(self.df_sample, self.boll_list_1) \
    or check_set_contains_list(self.df_sample, self.boll_list_2))
  if self.condition_1 or self.condition_2:
    return True
  else:
    return False


def oonoki(self, df, comments=True):
  # This function allows to decrease the size of DataFrame through the 
  # efficient type encoding of column types.
  self.mem_usg_before = memory_measure(df)
  if comments: print(f"Memory usage is: {self.mem_usg_before} MB")
  for col in df.columns: # change variable types to numeric to avoid incorrectly defined data type
    try:
      df[col] = pd.to_numeric(df[col], downcast='signed')
    except Exception:
      pass
  for col in df.columns: # encoding data types
    self.col_data_type = df[col].dtype
    try:     
      if self.col_data_type != 'object': # Non-objects (floats, integers, bool)
        max_number = df[col].max()
        min_number = df[col].min()
        if bool_check(self, df, col): # bool check and encoding
          df[col] = df[col].astype('bool')
        elif any_floats(df, col): # float check and encoding
          df[col] = pd.to_numeric(df[col], downcast='float') # выглядит так, словно надо допилить
        else: # integers check and encoding
          if min_number >= 0: # if all integers positive
            if max_number < 255:
              df[col] = df[col].astype(np.uint8) # from 0 to 255
            elif max_number < 65535:
              df[col] = df[col].astype(np.uint16) # from 0 to 65535
            elif max_number < 4294967295:
              df[col] = df[col].astype(np.uint32) # from 0 to 4294967295
            else:
              df[col] = df[col].astype(np.uint64) # from 0 to 18446744073709551615
          else: # if any integer is negative
            if min_number > np.iinfo(np.int8).min and max_number < np.iinfo(np.int8).max: # from -128 to 127
              df[col] = df[col].astype(np.int8)
            elif min_number > np.iinfo(np.int16).min and max_number < np.iinfo(np.int16).max: # from -32768 to 32767
              df[col] = df[col].astype(np.int16)
            elif min_number > np.iinfo(np.int32).min and max_number < np.iinfo(np.int32).max: # from -2147483648 to 2147483647
              df[col] = df[col].astype(np.int32)
            elif min_number > np.iinfo(np.int64).min and max_number < np.iinfo(np.int64).max: # from -9223372036854775808 to 9223372036854775807
              df[col] = df[col].astype(np.int64)  
      elif self.col_data_type == 'object': # Object check and encoding
        num_unique_values = df[col].nunique()
        if num_unique_values <= 15 or num_unique_values / len(df[col]) < 0.05:
          # if there are not so many unique variables (less than 15) or 
          # there are not so many unique variables (no more than 5%) 
          # then we set the categorical data type
          df[col] = df[col].astype('category')
      elif self.col_data_type == 'timedelta64[ns]' or self.col_data_type == 'm8[ns]': # timedelta check and encoding
        df[col] = pd.to_timedelta(df[col], errors='ignore')
      else: # datetime check and encoding
        df[col] = pd.to_datetime(df[col], errors='ignore')
    except Exception:
      if comments:
        print("******************************") 
        print("Проблема с декодированием: ", col)
        print(sys.exc_info())  
  # Print final result if comments==True
  if comments: print("___MEMORY USAGE AFTER COMPLETION:___")
  self.mem_usg_after = memory_measure(df)
  if comments: print(f"Memory usage is: {self.mem_usg_after} MB")
  if comments: print("This is ",round(100*self.mem_usg_after/self.mem_usg_before, 2),"% of the initial size")
  return df