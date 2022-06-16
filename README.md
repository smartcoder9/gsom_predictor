# gsom_predictor

### Outline
This is a model to predict the housing prices in the city of St.Petersburg, Russia. 

### Data
The data to build the model is taken from the Yandex Realty Database. It consists of various features such as Area, floor, rooms etc. and relates to the period between January 1, 2017 to August 1, 2018. The data was cleaned, outliers removed and split in two categories, namely- training and test data. 
Training data (approx 70% of the whole dataset) is chosen from January 1, 2017 to April 1, 2018 
Testing data (approx 30% of the whole dataset) is chosen from April 1, 2018 to August 1, 2018.

The dataset was cleaned in order to correct for missing data and avoid outliers

![image](https://user-images.githubusercontent.com/72549040/174079654-65388f14-971c-4aa2-be3a-aeea58449eb5.png)

![image](https://user-images.githubusercontent.com/72549040/174080194-925b4578-a136-45e9-8514-7de01ea8200d.png)



Below we can see some descriptive statistics

![image](https://user-images.githubusercontent.com/72549040/174080062-5e6a6809-0d7b-4eb2-8fd9-070ebe9b1f9d.png)

Here is how the correlation matrix look like

![image](https://user-images.githubusercontent.com/72549040/174080270-ada6e5d8-112a-4856-8fa1-aac7ede028aa.png)


Here is the relationship between the price of the apartment and the availability of the studio

![image](https://user-images.githubusercontent.com/72549040/174082235-ea6f84f4-b55b-449c-adf0-4246f99e4b03.png)



### ML Model and Train-test split
In this project, 2 models have been created. The first model is created using the Catboost regressor which includes the parameters- open plan, rooms, area, renovation. The catboost regressor algorithm is applied using the gradient boosting on decision trees to predict the prices. 

And the second model is created using the Random Forest regressor with parameters- floor, open plan, rooms, and area.

### Why two Models?
The primary reason is to cross-validate the results. Catboost is used for its ability to drastically reduce the error through gradient boosting and Random forest is used because it is appropriate when working with large data sets. Both the models have very low- MAE, MSE and RMSE.

### Model and Virtual Environment
It is possible to run the models on a virtual machine by installing the required python3 libraries- NumPy, Catboost, Flask and Skitlearn. Then, the following steps should be followed on VM.
1. Create a GIT folder on VM
2. Download folder from GitHub using command > python app.py
3. To run the app, use 5444 as the port
4. Select which model to run- 1 for the Random Forest and 2 for the catboost.
5. If an incorrect model is chosen, the app will return an error.
6. Then run the app on postman usinf the link below
		
		XX.XXX.XX.XXX:5444/predict_price?model=1&floor=1&open_plan=2&rooms=1&area=70&renovation=1

### Why use docker
Docker is an application that makes it possible to run app and save its prototype on different devices. A Dockerfile should be downloaded. This file inlcudes the commands required to build a container and make a copy of the application. 

### How to use Docker
To use docker, install and tune the application following the instructions here: [install docker on ubuntu tune the docker on ubuntu](https://docs.docker.com/engine/install/ubuntu/)

1. To build a container, use the following command

		docker build -t smartcoder9/gsom_predictor:v.1.0
	
2. To launch a container, use the following command

		docker run --network host -d smartcoder9/gsom_predictor:v.1.0
	
3. To see active container, use the following command
 
 		docker ps
	
4. To push to container, use the following command

		docker push myDockerLogin/myDockerfolder:v.X
	
	
### How can I download Docker on another Virtual Machine

Just download Docker application and use the following commnad, using the repository name and use Docker run
	
	git pull smartcoder9/gsom_predictor:v.1.0
	docker run --network host -d smartcoder9/gsom_predictor:v.1.0
	
Make a query by setting the values of the parameters as needed and start predicting!


### Contents of my docker file 

	MAINTAINER Madiya Bano
	RUN apt-get update -y
	COPY . /opt/gsom_predictor
	WORKDIR /opt/gsom_predictor
	RUN apt install -y python3-pip
	RUN pip3 install -r requirements.txt
	CMD python3 app.py
	
### Running an app using docker

Just pull the app from docker [gsom_predictor](https://hub.docker.com/repository/docker/madiya20/gsom_predictor) using the following commands
	
	#pull the app
	docker pull smartcoder9/gsom_predictor:v.1.0

	#run the app
	docker run --network host -d smartcoder9/gsom_predictor:v.1.0
