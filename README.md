# Indeed Job Extraction
![alt text](https://iili.io/H6LL26v.png)

## Part 1: Job Scraping
This part of the project focuses on scraping job data from Indeed using Selenium Grid, multiple proxies, and multi-threading. It is designed to scrape a large number of jobs efficiently and without IP blocking.

This process is divided into the following files:

#### app.py: 

This is the main file. It uses multi-threading and multiple proxies to extract data. It takes two parameters, job_number and num_threads, to control the volume and speed of data extraction.

#### driver.py: 

This file is responsible for creating the Chrome driver used in Selenium to interact with the Indeed website.

#### extract_data.py: 

This file defines the data extraction structure and dictates what data to pull from Indeed.

#### create_csv_file.py: 

This file creates a CSV file to store the extracted data.

#### output.csv: 

This is the CSV file where the data is stored.

Please see the following image for an overview of the process:

## Visite Selenium Grid Interface :

### http://srv2.omarelghiba.com:4444/

<img src="[https://github.com/favicon.ico](https://iili.io/H6QEYDg.png)" width="200">


## Part 2: HRflow.ai API
This part of the project focuses on storing the extracted data using the hrflow.ai API.

#### hrflow.py :

is responsible for this process. It uses the hrflow.ai API to send and store the scraped job data.

## Part 3: Deployment
The project is designed to be deployed using Docker, Docker Compose, and an Ubuntu Linux server.

It includes the following files for deployment:

#### Dockerfile: 

This file defines the Docker image for the project, specifying the environment in which the app runs.

#### docker-compose.yml: 

This file orchestrates the services that the application requires. It defines how Docker containers are built and how they interact with each other.

#### requirements.txt: 

This file lists all the Python libraries that your app depends on. When setting up the environment, Docker will use Pip to install these libraries.

## Running the Project

- docker compose up -d

