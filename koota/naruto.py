# надо привести все в божеский вид ( стоит ли вообще?)
import pandas as pd
from sklearn.preprocessing import LabelEncoder

def naruto(data, target='kavabanga', mario=True, ant_man=True, oonoki=True):
    sys = False # может есть нормальный способ проверить, установлена ли библиотека?
    
#*********************** Foundamental figures 
    data_length = len(data.index)
    
#*********************** Data preparation by additional functions    
    additional_func = [mario, #elimination of double spaces
                       ant_man, #lowering of letters
                       oonoki #
                       ]

    for func in additional_func:
        try:
            if func == True:
                data = func(data)
            else:
                pass
        except:
            if sys == False:
                import sys
                sys = True
            else:
                pass
            print(sys.exc_info())
            pass


    
#***********************************************************************************************************************************
    if target == 'kavabanga':
      pass
    else:
      data[target] = LabelEncoder().fit_transform(data[target])
    categorical_features = data.select_dtypes(exclude = ['number']).select_dtypes(exclude=['datetime']).columns
    for col in categorical_features:
        try:
            if data[col].dtype.name == 'category':
                data[col].cat.add_categories('unknown', inplace=True)
            else:
                pass
        except:
            pass
    data[categorical_features] = data[categorical_features].fillna('unknown')
    for col in categorical_features:
        if data[col].nunique() == 1:
            data[col] = LabelEncoder().fit_transform(data[col])
        elif 11 > data[col].nunique() >= 2:
            data = pd.get_dummies(data, columns=[col], prefix = [col+'_dummie_'])  
        else:
            variance = round(data[col].nunique() / data_length * 100, 2)
            if variance > 25: 
                print('В столбце ', col, "слишком много различных переменных - ", variance,'% от общего числа.')
            else:
                data[col] = LabelEncoder().fit_transform(data[col])
    return data.replace('unknown', np.nan)
