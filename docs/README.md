

This repo contains the final project for the course HHA 504: Cloud Computing Health Informatics Professionals. The project combines the tools and services explored in the course. 

# Table of Contents

1. [Web-Service](#web-service): contains a brief explanation of the product/web-service created for the project. 
2. [Technologies Used](#technologies-used): contains an explanation of the tools and services used in the web-service
3. [Steps to Running the Web-Service](#steps-to-running-the-web-service): steps to running the web-service either locally, using Docker, or deploying it on the cloud. 
4. [Environment Variables (.env) File Structure](#environment-variables-env-file-structure): contains the structure of the the .env file structure used in the product for the Google OAuth and MySQl connections. 
5. [Documentation of Screenshots](#documentation-of-screenshots): contains a brief explanation of the screenshots/videos included in the [docs](https://github.com/c-susan/flask_e2e_project/tree/main/docs) folder. 


## Web-Service
* The product created and documented in this repo is a very simple Flask app that displays data on air quality in New York City. Users can view a sample of New York City's air quality data from 2005 to 2021.
* The dataset used in this project was taken from Data.gov and contains information such as indicator/pollutant name, unit of measurement, geographical location it was measured at, and the date the data applies to. As the dataset contains 16218 rows, only a sample of 50 rows are displayed on the Flask app.

## Technologies Used
The tools and services used in this project include the following: 
1. Github - to version control the scripts 
2. Environment variables (.env) - to contain the credentials for Google OAuth and database connection strings for MySQL connection
3. Flask - the backend framework used in the web-service project to create a Flask app
4. Tailwind - the frontend framework for the web-service design
5. Azure Database for MySQL flexible server - database used in the project to include data into the Flask app
6. SQLAlchemy - the ORM used in the Flask app to create a connection with the MySQL database and query data.
7. Google OAuth - the authorization service used in the project to create a simple user authorization in the Flask app
8. Sentry.io - the logger service used in the project to log any issues in the web-service app
9. Docker - Docker was incorporated into the project to containerize the Flask app 
10. Cloud Deployment with Azure - the Flask app was deployed to the cloud using Microsoft Azure's App Services as another way of deploying the web application

## Steps to Running the Web-Service
The Flask web application can be deployed in 3 different ways: locally, using Docker, and cloud deployment with Azure. The following includes steps on how to run the application for each of the deployment ways. 
### Deploying Locally
1. To deploy the application locally, first clone the repo into your local environment in the terminal using: ```git clone https://github.com/c-susan/flask_e2e_project.git```
2. Once the repo is cloned onto your local environemnt, change your working directory to the `app` folder: ```cd flask_e2e_project/app```
3. In the terminal, run the application using ```python app.py```. The terminal will then create and show connection addresses which will bring you to the web application in another tab. 

### Deploying using Docker
The [app](https://github.com/c-susan/flask_e2e_project/tree/main/app) folder in the repo contains a Docker file which can be run to Dockerize the application. To Dockerize the application, make sure your working directory is in the [app](https://github.com/c-susan/flask_e2e_project/tree/main/app) folder with: ```cd flask_e2e_project/app```
1. Make sure to clone the repo into your local environment with ```git clone https://github.com/c-susan/flask_e2e_project.git``` and change your present working directory is in the app folder using: ```cd flask_e2e_project/app```
2. The first step to dockerizing the application is to create the Docker image. In the terminal, run: ```docker build -t <image-name> .```. Replace `<image-name>` with a name you want to call the Docker image.
3. Run ```docker images``` to cinfirm the image was successfully created. 
4. Once the image is create, you can run it with ```docker run -p 5000:5000 <image name>```. Replace `<image name>` in the code with the name you assigned to the docker image in the first step.

The following screenshot shows an example of how the application is Dockerized: 
<img width="900" alt="Docker" src="https://github.com/c-susan/flask_e2e_project/assets/123512714/bfc8f15d-a580-4f18-801a-bfe41b76e7a3">

### Cloud Deployment with Azure 
1. The application can be deployed to the cloud using Azure's App Services. First, clone the repo into your local environment and make sure to your present working directory is in the app folder.
2. In the terminal, install the Azure CLI using the command: ```curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash```
3. Wait for the Azure CLI and to confirm it was successfully installed, run: ```az```. The following snapshot shows the successful installation of the Azure CLI:
<img width="350" alt="azure" src="https://github.com/c-susan/flask_e2e_project/assets/123512714/60e971bf-91f9-494f-a417-f0d3253ad18e">

 4. In the terminal, run ```az login --use-device-code``` and follow the directions from the output to login to your Microsoft account and authenticate your device.
 5. Run the command: ```az webapp up --resource-group <resource-group> --name <app-name> --runtime PYTHON:3.9 --sku B1``` to create a web application on Azure. In the command, replace `<resource-group>` with your own Azure resource group and replace `<app-name>` with the name you want to assign to your web application.
 6. A new web service will be created. The following image shows a snapshot of my Flask app being deployed on Azure.
<img width="700" alt="cloud deployment" src="https://github.com/c-susan/flask_e2e_project/assets/123512714/936be703-69a3-406f-b4c6-bb728ebea118">

7. In your azure account, search 'App Services' in the search bar and then locate the web app created in the menu. 

The following shows a screenshot of the App Services menu in Azure with my created web application. Web-service link: [504flaskproject.azurewebsites.net](504flaskproject.azurewebsites.net)
<img width="800" alt="Screenshot 2023-12-15 at 10 25 29 PM" src="https://github.com/c-susan/flask_e2e_project/assets/123512714/95b7a461-c582-405b-93bd-8154ece7edd7">



## Environment Variables (.env) File Structure
Environment variables were used in the project to contain the credentials for Google OAuth and database connection strings for MySQL connection. The following is the template of the .env file structure used in the repo:

Connection for the MySQL Connection: 
```
DB_HOST = <azure-host-link>
DB_DATABASE = <database-name>
DB_USERNAME = <username>
DB_PASSWORD = <password>
DB_PORT = 3306
DB_CHARSET = utf8mb4
```

Credentials for Google OAuth
```
GOOGLE_CLIENT_ID = <client-id>
GOOGLE_CLIENT_SECRET = <client-secret>
```


## Documentation of Screenshots
This section contains a brief explanation of the screenshots included in this README.md file and the docs folder of the repo. 

### Screenshots of the Flask web application
Includes screenshots of each of the tabs in the application. 

#### Home Page:
<img width="600" alt="home:index_tab" src="https://github.com/c-susan/flask_e2e_project/assets/123512714/fbf7fb78-4f6d-4447-a472-1bc1a892cb6d">

#### Data Tab:
<img width="600" alt="data_tab" src="https://github.com/c-susan/flask_e2e_project/assets/123512714/837bae49-5ccc-43aa-9dcc-b705d583a85b">

#### Data Dictionary Tab:
<img width="600" alt="data_dict_tab" src="https://github.com/c-susan/flask_e2e_project/assets/123512714/10839eb7-a8f4-4792-9753-14b3e556bdc1">

#### Log-in Tab/Google OAuth:
<img width="600" alt="login_tab" src="https://github.com/c-susan/flask_e2e_project/assets/123512714/096ed205-d0de-4991-adac-155302cfd7dd">

#### Log-in Account Dashboard 
This snapshot shows the dashboard page when the user is authenticated through Google Oauth: 
<img width="600" alt="account" src="https://github.com/c-susan/flask_e2e_project/assets/123512714/1ef43aac-6d14-4f4b-9969-5fa99814f456">

### Data Dictionary
This image of the data dictionary for the NYC Air Quality dataset was included in the 'Data Dictionary' tab of the application. It was taken from: [NYC Open Data](https://data.cityofnewyork.us/Environment/Air-Quality/c3uy-2p5r).

<img width="400" alt="column-info" src="https://github.com/c-susan/flask_e2e_project/assets/123512714/4c84b063-436b-479d-9507-808731a15895">

### Azure App Services Menu
This is an example of what the Azure App Serives menu looks like with the created web application: 

<img width="600" alt="azure_app_services_menu" src="https://github.com/c-susan/flask_e2e_project/assets/123512714/5489aa50-d506-4319-9789-6d4ac3395817">

### Azure CLI
The screenshot shows a successful installation of Azure CLI when the ```az``` command is run: 

<img width="350" alt="azure_cli" src="https://github.com/c-susan/flask_e2e_project/assets/123512714/adfabab5-5747-4322-993f-132f364cfb51">


### Azure Cloud Deployment
The is the output shown when the web application is created and deployed using Azure when the follwing command is run: ```az webapp up --resource-group <resource-group> --name <app-name> --runtime PYTHON:3.9 --sku B1```:

<img width="600" alt="cloud_deployment" src="https://github.com/c-susan/flask_e2e_project/assets/123512714/2f67fa96-6d8f-44d1-b349-ec7055798256">


### Docker
This image shows what it looks like when the application is deployed using Docker. 

<img width="600" alt="Docker" src="https://github.com/c-susan/flask_e2e_project/assets/123512714/a75e8f32-8998-4b93-a7f1-17a367761177">

