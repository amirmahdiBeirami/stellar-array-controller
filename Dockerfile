# Dockerfile

# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any needed dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY stellar_controller.py .
# COPY test_controller.py . 

# Command to run the application when the container starts
# This will execute the if __name__ == "__main__": block in stellar_controller.py
CMD ["python", "stellar_controller.py"]
