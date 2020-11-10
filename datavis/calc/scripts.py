import pandas as pd

from sklearn import preprocessing
le = preprocessing.LabelEncoder()



def get_columns(request):
    df = pd.read_csv('../media/file.csv')
    col_list = df.columns()
    return col_list


def one_hot_encoding(col_list, prefix_list):
    res_df = df
    if(prefix_list):
        res_df = pd.get_dummies(df, columns=col_list, prefix = prefix_list)
    else:
        res_df = pd.get_dummies(df, columns=col_list)


def convertCategorical(col_list):

    for col in col_list:
        le.fit(df[col])
        df[col] = le.transform(df[col])
    
    print(df.head())