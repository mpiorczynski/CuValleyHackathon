from reader import read_and_remove_when_off

dirpath = "data/gz_files"
excel_filepath = "data/opis_zmiennych.xlsx"
temperature_filepath = "data/temp_zuz.csv"

df = read_and_remove_when_off(dirpath, excel_filepath, temperature_filepath)