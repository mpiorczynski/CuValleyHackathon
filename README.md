# CuValleyHackathon
## Golem team
### Team members: Mikołaj Piórczyński, Karol Rogoziński, Mateusz Borowski, Jędrzej Chmiel, Jakub Sobolewski

To start working with this model you need 4 things:
1) A directory with all gz_files like 'like 'avg_from_2020_10_01_00_00_00_to_2020_10_01_23_59_00.gz'
      IMPORTANT: In this directory there can't be any other files, like variables_description
2) An excel file in which there are variables description ('opis_zmiennych.xlsx')
3) A csv file in which there are heater temperatures ('temp_zuz.csv')
4) A .sav file in which there are stored parameters of xgboost model developed by us.

If you do not understand look on 'data' folder of this repository. There are all files you need.
WARNING: in data/gz_files directory there are only few files to preserve storage

Then you need to install all necessary dependencies and edit 4 variables in main.py file:
dirpath, excel_filepath, temperature_filepath, model_parametrs.
Each of this variable must store path to relevant file. (See comments in main.py file for more info)

Run main.py file and you are done!


### [Data Exploration](https://github.com/mpiorczynski/CuValleyHackathon/blob/main/data_exploration.ipynb)

### Presentation [PDF](https://github.com/mpiorczynski/CuValleyHackathon/blob/main/CuValley%20GOLEM.pdf), [PowerPoint](https://github.com/mpiorczynski/CuValleyHackathon/blob/main/CuValley%20GOLEM.pptx)

