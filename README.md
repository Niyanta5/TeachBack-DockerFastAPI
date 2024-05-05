# Running FastAPI Application with Docker Compose

## Prerequisites

Before you begin, ensure you have Docker Desktop and Docker Compose installed on your system.

## Steps

1. **Clone the Repository**: Clone the repository containing your FastAPI application code from GitHub.
    ```bash
    git clone https://github.com/Niyanta5/TeachBack-DockerFastAPI.git
    cd TeachBack-DockerFastAPI
    ```

2. **Configure Docker Compose**: Open the `docker-compose.yaml` file in your project directory and ensure it is configured correctly. This file should define the services required for running your FastAPI application, including any dependencies like databases.
    ```yaml
    version: '3'

    services:
      web:
        build: .
        command: uvicorn main:app --reload --host 0.0.0.0 --port 8000
        ports:
          - 8000:8000
    ```
    Ensure that the `build` section points to the directory containing your Dockerfile and application code.

3. **Build and Run Docker Compose**: Run the following command to build and run the Docker containers defined in the `docker-compose.yaml` file.
    ```bash
    docker-compose up --build
    ```
    This command will build the Docker image for your FastAPI application, create and start the Docker container, and expose port 8000 on your localhost for accessing the FastAPI application.

4. **Access FastAPI Application**: Once the Docker containers are running, you can access your FastAPI application in your browser at http://localhost:8000/docs.
