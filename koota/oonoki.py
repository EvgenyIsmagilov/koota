# coding: utf-8
import pandas as pd
import numpy as np

# class koota:
#     def __init__(self)


def oonoki(data):

    import sys
    start_mem_usg = round(data.memory_usage().sum() / 1024**2, 2)
    print("Memory usage of properties dataframe is :",start_mem_usg," MB")
    NAlist = [] # Keeps track of columns that have missing values filled in. 
    for col in data.columns: # если тип данных определен неверно, то мы это поправим
        try:
            data[col] = pd.to_numeric(data[col], downcast='signed')
        except:
            pass
#**********************************************************************************************
    for col in data.columns:
        try:
#****************************************** Проверка на наличие странных чисел и пропусков + определение типа днных (float or integer)           
            if data[col].dtype != 'object':  
                # print("Column: ", col)
                # print("dtype before: ",data[col].dtype)

                # make variables for Int, max and min
                IsInt = False
                mx = data[col].max()
                mn = data[col].min()
                
                # Есть ли пропуски и странные числа?
                if not np.isfinite(data[col]).all(): 
                    NAlist.append(col)
                    data[col].fillna(mn-1,inplace=True)  
                    
                # Проверка действительно ли число является целым, али шпион float
                asint = data[col].fillna(0).astype(np.int64)
                result = (data[col] - asint)
                result = result.sum()
                if 0.0001 > result > -0.0001:
                    IsInt = True
#****************************************** Колдуем с типом данных
                # Integer
                if IsInt: 
                    if mn >= 0:
                        if mx < 255:
                            data[col] = data[col].astype(np.uint8) # от 0 до 255
                        elif mx < 65535:
                            data[col] = data[col].astype(np.uint16) # от 0 до 65535
                        elif mx < 4294967295:
                            data[col] = data[col].astype(np.uint32) # от 0 до 4294967295
                        else:
                            data[col] = data[col].astype(np.uint64) # от 0 до 18446744073709551615
                    else:
                        if mn > np.iinfo(np.int8).min and mx < np.iinfo(np.int8).max: # от -128 до 127
                            data[col] = data[col].astype(np.int8)
                        elif mn > np.iinfo(np.int16).min and mx < np.iinfo(np.int16).max: # от -32768 до 32767
                            data[col] = data[col].astype(np.int16)
                        elif mn > np.iinfo(np.int32).min and mx < np.iinfo(np.int32).max: # от -2147483648 до 2147483647
                            data[col] = data[col].astype(np.int32)
                        elif mn > np.iinfo(np.int64).min and mx < np.iinfo(np.int64).max: # от -9223372036854775808 до 9223372036854775807
                            data[col] = data[col].astype(np.int64)    
                
                # Float
                else:
                    data[col] = pd.to_numeric(data[col], downcast='float')
#****************************************** Колдуем с типом данных
            else:
                num_unique_values = len(data[col].unique())
                num_total_values = len(data[col])
                if num_unique_values / num_total_values < 0.5:
                    # print("Column: ", col)
                    data[col] = data[col].astype('category')
                else:
                    # print("Column: ", col)
                    data[col] = pd.to_datetime(data[col], errors='ignore')

            # Print new column type
            # print("dtype after: ",data[col].dtype)
            # print("******************************")
        except:
            print("******************************") 
            print("Косяк с : ", col)
            print(sys.exc_info())  
    # Print final result
    print("___MEMORY USAGE AFTER COMPLETION:___")
    mem_usg = round(data.memory_usage().sum() / 1024**2, 2)
    print("Memory usage is: ",mem_usg," MB")
    print("This is ",round(100*mem_usg/start_mem_usg, 2),"% of the initial size")
    return data, NAlist
