# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

RUN pip install --upgrade pip
# Install any needed packages specified in requirements.txt
RUN pip install undetected_chromedriver selenium pandas pyspark

# Copy the Python files into the container at /app
COPY . /app/


CMD ["python", "g2_data.py", "python", "getapp.py", "python", "sparkjob.py"]


