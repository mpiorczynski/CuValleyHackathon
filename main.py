from reader import read_and_remove_when_off
from wheather_reader import read

dirpath = "data/gz_files"
excel_filepath = "data/opis_zmiennych.xlsx"
temperature_filepath = "data/temp_zuz.csv"

filepaths_encoding = [('data/wheather/s_d_t_415_2020.csv', 'utf-8'), ('data/wheather/s_d_t_415_2021.csv', 'utf-8'),
                      ('data/wheather/s_d_t_01_2022.csv', 'ANSI')]

df_all = read_and_remove_when_off(dirpath, excel_filepath, temperature_filepath)
#this is dataframe with all features (except wheather) combined to one dataframe

wheather_df = read(filepaths_encoding)
#this is dataframe containing temperature, humidity and pressure from LEGNICA from years 2020, 2021 and 2022
