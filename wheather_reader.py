import pandas as pd
import numpy as np

def read_wheather(filepaths_encoding):
    """filepaths_encoding is list of tuples of filepath to csv file from imgw (more in readmi file) and
    encoding of this file"""

    dataframes = []
    for filepath, encoding in filepaths_encoding:
        names = ['station_name','year', 'month', 'day', 'temperature', 'cisnienia_pary_wodnej', 'wilgotnosc_wzgledna',
                 'cisnienie_na_poziomie_stacji']
        df = pd.read_csv(filepath, usecols=[1,2,3,4,9,11,13,15], encoding=encoding, names=names)
        df = df.loc[df['station_name'] == 'LEGNICA']
        df['index'] = pd.to_datetime(df[['year', 'month', 'day']])
        df.drop(columns = ['year', 'month', 'day', 'station_name'], inplace=True)
        df.set_index('index', inplace=True)
        dataframes.append(df)
    return pd.concat(dataframes, axis=0)

filepaths_encoding = [('2-piec/s_d_t_415_2020.csv', 'utf-8'), ('2-piec/s_d_t_415_2021.csv', 'utf-8'),
                      ('2-piec/s_d_t_01_2022.csv', 'ANSI')]

def to_hours(df):
    """after calling a read_weather function we have dataframe with whather data, but only for each day. We need
    for each hour. This function takes dataframe describing weather for each day and returns dataframe describing
    a weather of each hour of each day. (it assumes that all day weather was the same)"""

    days = []
    for i in range(df.shape[0]):
        new_df = df.iloc[i:i+1, :]
        new_df.reset_index(inplace=True)
        new_df = pd.concat([new_df]*24)
        new_df.reset_index(inplace=True, drop=True)
        new_df['hour'] = pd.Series(data=np.arange(24), index=new_df.index)
        new_df['date_time'] = pd.to_datetime(new_df['index'].astype(str), format='%Y-%m-%d') +\
                               pd.to_timedelta(new_df['hour'], unit='h')
        new_df.set_index('date_time', inplace=True, drop=True)
        new_df.drop(columns=['index', 'hour'], inplace=True)
        days.append(new_df)
    return pd.concat(days)

def read(filepaths_encoding):
    df = read_wheather(filepaths_encoding)
    df = to_hours(df)
    return df

