FROM python:3.8.10-slim   # Base image using Python 3.8.10 slim version

WORKDIR /app   # Set the working directory inside the container to /app

COPY . /app   # Copy the local directory (containing FastAPI application files) to the /app directory in the container

RUN pip install -r requirements.txt   # Install dependencies listed in requirements.txt file using pip
