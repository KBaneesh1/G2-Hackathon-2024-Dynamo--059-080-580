# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY . /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Python files into the container at /app
COPY script1.py script2.py script3.py /app/

# Run all Python scripts sequentially when the container launches
CMD ["python", "g2_data.py", "&&", "python", "script2.py", "&&", "python", "script3.py"]
