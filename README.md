# Repo README

This repository contains scripts and configurations for fetching data from G2, scraping data from GetApp, and processing the data using PySpark. Below is a detailed explanation of each file included in this repository along with instructions on how to run them.

## Files

### g2_data.py

This Python script fetches product data from the G2 API using an API token and saves the response to a JSON file. It iterates through multiple pages of the API response until all products are fetched.


```bash
python g2_data.py

getapp.py
This script scrapes product data from the GetApp website using Selenium with an undetected ChromeDriver. It saves the scraped data to a JSONL file containing one JSON record per line.

To run:
bash
python getapp.py

sparkjob.py
This PySpark script preprocesses the scraped JSONL file, converts it to a JSON file, and performs data manipulation tasks. It then writes the final result to a CSV file.

python sparkjob.py

Dockerfile
This Dockerfile defines a Docker image containing all the necessary dependencies to run the Python scripts. It installs Python dependencies, copies the script files into the container, and runs the scripts sequentially.

cronjob.yml
This YAML file defines a Kubernetes CronJob that schedules the execution of the Python scripts at regular intervals using the Docker image built from the provided Dockerfile.

Output Files
trip.json
This file contains the raw JSON response fetched from the G2 API by g2_data.py.

All_products.jsonl
This file contains the scraped product data from GetApp in JSONL format.

preprocessed_products_website.jsonl
This file contains the preprocessed JSONL data, with each JSON record on a separate line.

ip.json
This file contains the JSON data converted from JSONL, ready for processing by PySpark.

out1.csv
This CSV file contains intermediate data processed by PySpark.

out_final.csv
This CSV file contains the final processed data after joining and manipulation tasks performed by PySpark.

Running the Scripts
To run the scripts, ensure you have Python installed on your system. If you're using Docker, make sure Docker is installed as well.

Clone this repository to your local machine.
Navigate to the repository directory.
Run the Python scripts sequentially:
bash

python g2_data.py
python getapp.py
python sparkjob.py
or build and run the Docker image:
bash

docker build -t my-python-app .
docker run my-python-app
Check the output files generated in the repository directory.
Running with Kubernetes CronJob
To run the scripts automatically at regular intervals using Kubernetes, follow these steps:

Ensure you have a Kubernetes cluster set up and kubectl configured.
Apply the CronJob configuration:
bash

kubectl apply -f cronjob.yml
This will create a CronJob named my-python-cronjob.
Monitor the logs of the CronJob to see the execution output:
bash

kubectl logs -f <pod_name>
Replace <pod_name> with the actual name of the pod created by the CronJob.
That's it! You've successfully set up automated data fetching and processing using Kubernetes CronJob.
