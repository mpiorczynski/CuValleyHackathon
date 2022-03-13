from reader import read
import pickle
import xgboost as xgb

from sklearn.metrics import mean_squared_error

#For this file to work you need to have 4 things:
# 1) A directory with all gz_files like 'like 'avg_from_2020_10_01_00_00_00_to_2020_10_01_23_59_00.gz'
#       IMPORTANT: In this directory there can't be any other files, like variables_description
#       Store path to this directory in dirpath variables
# 2) An excel file in which there are variables description ('opis_zmiennych.xlsx')
#       Store path to this file in excel_filepath variable.
# 3) A csv file in which there are heater temperatures ('temp_zuz.csv')
#       Store path to this file in temperature_filepath variable.
#4) A .sav file in which there are stored paraeters of xgboost model developed by us.
#       Store path to this file in model_parametrs variable.

dirpath = "data/gz_files"
excel_filepath = "data/opis_zmiennych.xlsx"
temperature_filepath = "data/temp_zuz.csv"
model_parametrs = 'data/model.sav'
#here are those three importat variables


df = read(dirpath, excel_filepath, temperature_filepath)
# A simple function from prepered by us module read all necessary information into one pandas dataframe.
print("The data was loaded from files using 'reader' model. \n")

X = df.drop(columns=['temp_zuz'])
y_true = df['temp_zuz'].values
#Now it's time to split this dataframe to features and labels. Those two lines above are enough


pipe = pickle.load(open(model_parametrs, 'rb'))
#Reading model from file.
print("The xgboost model was loaded using saved parameters. \n")


#Now let's use hour model on this data and test it.
y_pred = pipe.predict(X)
mse = mean_squared_error(y_true, y_pred)

print("The model was tested on above_mentioned data. \n"
      "The MSE score of the model is: ", mse)
