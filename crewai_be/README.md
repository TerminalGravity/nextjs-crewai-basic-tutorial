# CrewAI Flask API Backend

Welcome to the CrewAI Flask API Backend, the core interface for the Next.js web application. This Python-based backend leverages Flask to provide a robust API layer, facilitating seamless interactions between the frontend and various data sources. Below you'll find instructions for setting up and running the backend.

## Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.10 or higher
- Poetry for Python package management

## Setup Instructions

2. **Install Dependencies**: This command installs all dependencies defined in `pyproject.toml` without installing the project package itself & sources the venv . run the following command to install the required Python packages:
poetry install --no-root

3. **Use POETRY env shell interpreter**
poetry shell
-> make IDE interpreter go to shell path

4. **Run Flask Server**
This command launches the Flask server, making the API accessible for the Next.js frontend application.
poetry run python api.py


## Project Structure

The CrewAI Flask API Backend is organized into several key components, each serving a distinct role in the application's functionality:

- `api.py`: Serves as the gateway for incoming requests. It defines the Flask app and routes requests to the appropriate handlers.

- `tasks.py`: Manages asynchronous tasks such as scheduled jobs or background processes that need to run independently of user requests.

- `tools/`: A directory containing utility scripts and helper functions. These tools support various operations such as data parsing, validation, and other common tasks.

- `agents.py`: Responsible for interfacing with external data sources and APIs. Agents fetch, process, and relay data to and from third-party services.

- `crew.py`: Contains the core business logic of the application. It processes data, implements the main features, and handles the logic specific to the CrewAI operations.

- `job_manager.py`: Oversees job-related operations, including the creation, monitoring, and management of jobs. It ensures that tasks are executed in order and resources are allocated efficiently.

- `models.py`: Defines the data models and structures used throughout the application. This includes representations of database tables and complex data types.





