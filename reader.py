import pandas as pd
import os
import numpy as np

def read_dataframe(dirpath, excel_file_path, temperature_file_path):
    """This function creates a pandas dataframe in which there are given temperature and other data as
    'TEMP.11 POD 2 WARSTWĄ WYMURÓWKI' and so on. The index is timestamp. Each index is given hour in given day.

    dirpath is directory to folder, where are all .gz files, like 'avg_from_2020_10_01_00_00_00_to_2020_10_01_23_59_00.gz'
    in this directory there can't be any other files, like variables_description

    excel_file_path is filepath to excel file with variables descriptions

    temperature_file_path is filepath to .csv file with temperature of heater
    """


    df = pd.concat([pd.read_csv(os.path.join(dirpath, fname))
                for fname in os.listdir(dirpath)], ignore_index=True)

    df['czas'] = df['czas'].str[:19]
    df['czas'] = pd.to_datetime(df['czas'], format='%Y-%m-%d %H:%M:%S')

    col_df = pd.read_excel(excel_file_path)
    col_df['opis'] = col_df['opis'] + ' ' + col_df['Jednostka']
    col_df.drop(columns=['Jednostka'], inplace=True)

    names_dict = col_df.set_index('Tagname').to_dict()['opis']
    names_dict =  {k.lower(): v for k, v in names_dict.items()}

    df.rename(columns=names_dict, inplace=True)

    temp = pd.read_csv(temperature_file_path, delimiter=';')
    temp.rename(columns={'Czas': 'czas'}, inplace=True)
    temp['czas'] = pd.to_datetime(temp['czas'])
    merged = pd.merge(df, temp, how='left', on='czas')

    return merged

def remove_when_off(df, min_off=1270, margin=15, by='temp_zuz'):
    """This function removes from given data dataframes all records when heater was off. It remove all records in which
    given feater (described by by argument) was lower or equal to min_off plus margin number of records below or after
    this record.

    Return:
        Function returns view on new dataframe whem heater was off

    """

    what = np.full(df.shape[0], True)
    temp_series = df[by]
    max_idx = df.shape[0] - 1
    for index, (date, temp) in enumerate(temp_series.iteritems()):
        if temp <= min_off:
            from_idx, to_idx = index - margin, index + margin
            if from_idx < 0: from_idx = 0
            if to_idx > max_idx: to_idx = max_idx
            what[from_idx:to_idx] = False
    return df[what]

def read_and_remove_when_off(dirpath, excel_file_path, temperature_file_path):
    """This function read dataframes from files and then remove"""

    df = read_dataframe(dirpath, excel_file_path, temperature_file_path)
    return remove_when_off(df)