# gsom_predictor

### Outline
This is a model to predict the housing prices in the city of St.Petersburg, Russia. 

### Data
The data to build the model is taken from the Yandex Realty Database. It consists of various features such as Area, floor, rooms etc. and relates to the period between January 1, 2017 to August 1, 2018. The data was cleaned, outliers removed and split in two categories, namely- training and test data. Training data is chosen from January 1, 2017 to April 1, 2018 and test data is chosen from April 1, 2018 to August 1, 2018.
The dataset was cleaned in order to correct for missing data and avoid outliers


![image](https://user-images.githubusercontent.com/72549040/174079654-65388f14-971c-4aa2-be3a-aeea58449eb5.png)




### ML Model
In this project, 2 models have been created. The first model is created using the Catboost regressor which includes the parameters- open plan, rooms, area, renovation and the second model is created using the Random Forest regressor with parameters- floor, open plan, rooms, and area.

### Why two Models?
The primary reason is to cross-validate the results. Catboost is used for its ability to drastically reduce the error through gradient boosting and Random forest is used because it is appropriate when working with large data sets. Both the models have very low- MAE, MSE and RMSE.

### Model and Virtual Environment
It is possible to run the models on a virtual machine by installing the required python3 libraries- NumPy, Catboost, Flask and Skitlearn. Then, the following steps should be followed on VM.
1. Create a GIT folder on VM
2. Download folder from GitHub using command > python app.py
3. To run the app, use 5444 as the port
4. Select which model to run- 1 for the Random Forest and 2 for the catboost.



