# Use the official Airflow image as a parent image
FROM apache/airflow:2.3.0

# Set the working directory in the container
WORKDIR /opt/airflow

# Install additional dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
