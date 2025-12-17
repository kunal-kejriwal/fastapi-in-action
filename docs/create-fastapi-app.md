# Creating and Running a FastAPI Application

This document explains how to create a basic FastAPI application,
install the required dependencies, and run the application locally
using the command-line interface (CLI).

---

## Prerequisites

Ensure you have the following installed:

- Python 3.9 or higher
- pip (Python package manager)
- A terminal or command prompt

Verify Python installation:

python --version

Step 1: Create a Virtual Environment (Recommended) 

        1. Create a virtual environment to isolate dependencies:
                python -m venv venv
        2. Activate the virtual environment:
                1. Windows - venv\Scripts\activate
                2. MacOS - source venv/bin/activate

Step 2: Install FastAPI and Uvicorn

    Install FastAPI and the ASGI server Uvicorn:

        1. Open Terminal -> pip install fastapi uvicorn
        2. Verify Installation
            pip show fastapi
            pip show uvicorn

Step 3: Create a Basic FastAPI Application

    Create a Python file named main.py:

        1. Import FastAPI. 
            from fastapi import FastAPI
        2. instantiate app. 
            app = FastAPI()
        3. Define your first endpoint
            @app.get("/first-api-endpoint")
        4. Define the function with async keyword. 
            async def first_api_endpoint():
                return

Step 4: Run the Application

    Start the FastAPI application using Uvicorn: 
        uvicorn main:app --reload
            main → Python file name (main.py)

            app → FastAPI instance inside the file

            --reload → Automatically reloads the server on code changes

Step 5: Access the Application

    Once the server starts, access the following URLs:
        1. Application endpoint - http://127.0.0.1:8000/
        2. Interactive API documentation (Swagger UI) - http://127.0.0.1:8000/docs
        3. Alternative API documentation (ReDoc) - http://127.0.0.1:8000/redoc

Step 6: Stopping the Server

    To stop the server, press: "CTRL + C" on the terminal. 




Notes

    1. FastAPI automatically generates OpenAPI documentation.

    2. Uvicorn is an ASGI server optimized for high-performance async applications.

    3. The --reload flag should be used only in development environments.